import re
import os
import uuid
import utils
import PyPDF2
import conexaoDB
import integradorE2DOC
from datetime import datetime
from tkinter import messagebox



def executar_automacao(arquivos_comprovante):
    tipo_pag_incorreto = []
    cpfs_errados = []
    comp_nao_env = []
    relatorio = []

    cliente = integradorE2DOC.E2DocClient()

    conectado = cliente.autenticar()
    if conectado == "Conexão não estabelecida entre os sistemas":
        messagebox.showerror("Erro!", "Conexão não estabelecida com o E2DOC.")
        raise Exception("Conexão não estabelecida com o E2DOC")

    agora = datetime.now()
    data_formatada = agora.strftime("%Y-%m-%d")
    data_formatada = str(data_formatada)
    data_festiva = agora.strftime("%d/%m")
    data_festiva = str(data_festiva)


    for caminho in arquivos_comprovante:
        banco = utils.retornar_banco(caminho)

        # DADOS PERTINENTES PARA A MANIPULAÇÃO DOS ARQUIVOS 
        data_de_pagamento = re.search(r"\b\d{2}-\d{2}\b", caminho).group()  # 16-12
        competencia = re.search(r"\b\d{4}\\\d{2}\b", caminho).group()
        ano = competencia.split("\\")[0]
        ano_vigente = ano   # 2024
        mes = competencia.split("\\")[1]
        mes_vigente = utils.retornar_mes(mes)   # 12 - DEZEMBRO
        competencia = competencia.split("\\")[1] + "/" + competencia.split("\\")[0]     # 12/2024


        with open(caminho, 'rb') as file:

            reader = PyPDF2.PdfReader(file)
            
            num_pages = len(reader.pages)
            
            for page_num in range(num_pages):
                
                page = reader.pages[page_num]
                writer = PyPDF2.PdfWriter()
                writer.add_page(page)
                texto = page.extract_text().replace(" ", "").upper()
                manual = re.search(r"CHAVE\d{11}[A-Z0-9]{3}", texto)
                manual_pedido = re.search(r"CHAVE\d{11}[A-Z0-9]{3}[A-Za-z0-9]+", texto)

                if manual or manual_pedido:
                    
                    # DADOS PERTINENTES PARA O E2DOC E PARA A DISTRIBUICAO DOS ARQUIVOS
                    if manual_pedido:
                        chave = manual_pedido.group()
                        pedido = chave[-6:].upper()
                        tipo_pagamento = chave[-9:-6]
                    else:
                        chave = manual.group()
                        tipo_pagamento = chave[-3:]

                    cpf = chave[5:16]
                    try:
                        regiao, centro_de_custo, nome = conexaoDB.consultar_db(cpf)
                    except:
                        messagebox.showerror("Erro!", "Não foi possivel se conectar ao bando de dados da empresa.")
                        raise Exception("Não foi possivel se conectar ao bando de dados da empresa.")
                    
                    if regiao == False:
                        cpfs_errados.append(cpf)

                    nome_arquivo = nome + ".pdf"
                    if banco == "SANTANDER":
                        nome_arquivo = nome + " - OP DISPONIVEL.pdf"

                    if tipo_pagamento == "131" and mes_vigente != "11 - NOVEMBRO":
                        tipo_pagamento == "13A"
                    
                    if tipo_pagamento == "132" and mes_vigente != "12 - DEZEMBRO":
                        tipo_pagamento == "13A"


                    match tipo_pagamento:
                        case 'LOC':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante Frota\LOCAÇÃO VEICULO\MANUAL"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento)   
                            modelo_de_documento = 'LOCAÇÃO'
                            
                        case 'VAT':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante Beneficios\VALE TRANSPORTES"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='VT', pedido=pedido)   
                            modelo_de_documento = 'VT'

                        case 'VAR':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante Beneficios\VALE ALIMENTACAO"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='VA', pedido=pedido)
                            modelo_de_documento = 'VA'

                        case 'FOL':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\PROVENTOS\PAGTOS MANUAIS"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo="FOLHA GERAL")
                            modelo_de_documento = 'PROVENTOS'

                        case 'ARV':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\PROVENTOS\PAGTOS MANUAIS"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo="ADTO REVAP")
                            modelo_de_documento = 'PROVENTOS'

                        case 'ARP':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\PROVENTOS\PAGTOS MANUAIS"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo="ADTO REPAR")
                            modelo_de_documento = 'PROVENTOS'
                        
                        case '13A':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\13 SALARIO"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='13 SALARIO')
                            modelo_de_documento = '13 SALARIO'

                        case '131':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\13 SALARIO"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='1ª 13 SALARIO')
                            modelo_de_documento = '13 SALARIO'

                        case '132':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\13 SALARIO"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='2ª 13 SALARIO')
                            modelo_de_documento = '13 SALARIO'
                        
                        case '13T':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\13 SALARIO"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='TJ 13 SALARIO')
                            modelo_de_documento = '13 SALARIO'
                        
                        case 'RES':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\RESCISOES"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento)
                            modelo_de_documento = 'RESCISÕES'

                        case 'FER':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\FERIAS"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento)
                            modelo_de_documento = 'FÉRIAS'

                        case 'FGT':
                            diretorio_destino = r"C:\Users\User\EQS Engenharia Ltda\Comprovantes - Comprovante DP\MULTA FGTS"
                            diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento)
                            modelo_de_documento = 'MULTAS DE FGTS RESCISÓRIA'

                        case _:
                            tipo_pag_incorreto.append(chave)


                    caminho_arq = os.path.join(diretorio_destino, nome_arquivo)
                    

                    if chave not in tipo_pag_incorreto and cpf not in cpfs_errados:
                        with open(caminho_arq, 'wb') as arq_saida:
                            writer.write(arq_saida)


                        # PARTE DO E2DOC

                        conteudo_base64, hash_md5, tamanho = utils.ler_arquivo(caminho_arq)
                        protocolo = str(uuid.uuid4())
                        file_name = protocolo + "_1_0.pdf"

                
                        match tipo_pagamento:
                            case 'FOL':
                                competencia_folha = int(competencia.split("/")[0])
                                competencia_folha -= 1
                                competencia_folha = str(competencia_folha) + "/" + competencia.split("/")[1]
                                try:
                                    cliente.iniciar_sincronismo(protocolo, competencia_folha, cpf, nome, banco, regiao, centro_de_custo)
                                    cliente.enviar_partes_do_arquivo(file_name, conteudo_base64)
                                    cliente.efetivar_envio(modelo_de_documento, data_formatada, hash_md5, tamanho)
                                    cliente.finalizar_envio()
                                except Exception as e:
                                    comp_nao_env.append([nome, modelo_de_documento, chave, e])
                            
                            case 'LOC':
                                try:
                                    cliente.iniciar_sincronismo(protocolo, competencia, cpf, nome, banco, regiao, centro_de_custo, modelo_de_pasta='FINANCEIRO - FROTA', label='Diferente')
                                    cliente.enviar_partes_do_arquivo(file_name, conteudo_base64)
                                    cliente.efetivar_envio(modelo_de_documento, data_formatada, hash_md5, tamanho, modelo_de_pasta='FINANCEIRO - FROTA')
                                    cliente.finalizar_envio()
                                except Exception as e:
                                    comp_nao_env.append([nome, modelo_de_documento, chave, e])
                            
                            case 'VAR' | 'VAT':
                                try:
                                    cliente.iniciar_sincronismo(protocolo, competencia, cpf, nome, banco, regiao, centro_de_custo, modelo_de_pasta='FINANCEIRO - BENEFICIOS', label='Diferente', pedido=pedido)
                                    cliente.enviar_partes_do_arquivo(file_name, conteudo_base64)
                                    cliente.efetivar_envio(modelo_de_documento, data_formatada, hash_md5, tamanho, modelo_de_pasta='FINANCEIRO - BENEFICIOS')
                                    cliente.finalizar_envio()
                                except Exception as e:
                                    comp_nao_env.append([nome, modelo_de_documento, chave, e])
                                
                            case _:
                                try:
                                    cliente.iniciar_sincronismo(protocolo, competencia, cpf, nome, banco, regiao, centro_de_custo)
                                    cliente.enviar_partes_do_arquivo(file_name, conteudo_base64)
                                    cliente.efetivar_envio(modelo_de_documento, data_formatada, hash_md5, tamanho)
                                    cliente.finalizar_envio()
                                except Exception as e:
                                    comp_nao_env.append([nome, modelo_de_documento, chave, e])

                        if chave not in comp_nao_env:
                            relatorio.append([nome, "  -  ", modelo_de_documento, "  -  ", competencia])
                                

    utils.enviar_email(relatorio, data_festiva)     
    
    return relatorio, tipo_pag_incorreto, cpfs_errados, comp_nao_env
      
