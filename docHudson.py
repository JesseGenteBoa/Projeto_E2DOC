import re
import os
import uuid
import utils
import PyPDF2
import conexaoDB
import integradorE2DOC
from datetime import datetime



tipo_pag_incorreto = []

cliente = integradorE2DOC.E2DocClient()


conectado = cliente.autenticar()


agora = datetime.now()
data_formatada = agora.strftime("%Y-%m-%d")
data_formatada = str(data_formatada)


# Caminho da pasta onde estão os arquivos
caminho = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Financeiro - COMPROVANTES - DESMEMBRAR\2024\12 DEZEMBRO\ITAU\16-12\COMPROVANTES PIX 16-12.pdf"

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
        texto = page.extract_text().replace(" ", "")
        manual = re.search(r"\b\d{11}_[A-Z0-9]{2}\b", texto)
        manual_pedido = re.search(r"\b\d{11}_[A-Z0-9]{2}_[A-Za-z0-9]+\b", texto)

        if manual or manual_pedido:
            
            # DADOS PERTINENTES PARA O E2DOC E PARA A DISTRIBUICAO DOS ARQUIVOS
            if manual_pedido:
                chave = manual_pedido.group()
                pedido = chave.split("_")[2].upper()
            else:
                chave = manual.group()
            cpf = chave.split("_")[0]
            tipo_pagamento = chave.split("_")[1].upper()
            regiao, centro_de_custo, nome = conexaoDB.consultar_db(cpf)
            nome_arquivo = nome + ".pdf"
            if banco == "SANTANDER":
                nome_arquivo = nome + " - OP DISPONIVEL.pdf"

            match tipo_pagamento:
                case 'LO':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante Frota\LOCAÇÃO VEICULO\MANUAL"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento)   
                    modelo_de_pasta = 'FINANCEIRO - FROTA'
                    modelo_de_documento = 'LOCAÇÃO'
                    
                case 'VT':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante Beneficios\VALE TRANSPORTES"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='VT', pedido=pedido)   
                    modelo_de_pasta = 'FINANCEIRO - BENEFICIOS'
                    modelo_de_documento = 'VT'

                case 'VA':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante Beneficios\VALE ALIMENTACAO"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='VA', pedido=pedido)
                    modelo_de_pasta = 'FINANCEIRO - BENEFICIOS'
                    modelo_de_documento = 'VA'

                case 'FO':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\PROVENTOS\PAGTOS MANUAIS"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo="FOLHA GERAL")
                    modelo_de_documento = 'PROVENTOS'

                case 'RV':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\PROVENTOS\PAGTOS MANUAIS"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo="ADTO REVAP")
                    modelo_de_documento = 'PROVENTOS'

                case 'RP':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\PROVENTOS\PAGTOS MANUAIS"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo="ADTO REPAR")
                    modelo_de_documento = 'PROVENTOS'
                
                case 'AD':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\13 SALARIO"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='13 SALARIO')
                    modelo_de_documento = '13 SALARIO'

                case '1P':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\13 SALARIO"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='1ª 13 SALARIO')
                    modelo_de_documento = '13 SALARIO'

                case '2P':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\13 SALARIO"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='2ª 13 SALARIO')
                    modelo_de_documento = '13 SALARIO'
                
                case 'TJ':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\13 SALARIO"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='TJ 13 SALARIO')
                    modelo_de_documento = '13 SALARIO'
                
                case 'RE':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\RESCISOES"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento)
                    modelo_de_documento = 'RESCISÕES'

                case 'FE':
                    diretorio_destino = r"C:\Users\User\OneDrive - EQS Engenharia Ltda\Área de Trabalho\Pasta Simulação\Comprovantes - Comprovante DP\FERIAS"
                    diretorio_destino = utils.criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento)
                    modelo_de_documento = 'FÉRIAS'

                case _:
                    tipo_pag_incorreto.append(chave)
                    print(chave + " não é um tipo de pagamento válido.\n")
                    # AINDA FALTA O DO FGTS


            caminho_arq = os.path.join(diretorio_destino, nome_arquivo)
            

            if chave not in tipo_pag_incorreto:
                with open(caminho_arq, 'wb') as arq_saida:
                    writer.write(arq_saida)


                # PARTE DO E2DOC

                conteudo_base64, hash_md5, tamanho = utils.ler_arquivo(caminho_arq)
                protocolo = str(uuid.uuid4())
                file_name = protocolo + "_1_0.pdf"

           
                match tipo_pagamento:
                    case 'FO':
                        competencia_folha = int(competencia.split("/")[0])
                        competencia_folha -= 1
                        competencia_folha = str(competencia_folha) + "/" + competencia.split("/")[1]
                        cliente.iniciar_sincronismo(protocolo, competencia_folha, cpf, nome, banco, regiao, centro_de_custo)
                        cliente.enviar_partes_do_arquivo(file_name, conteudo_base64)
                        cliente.efetivar_envio(modelo_de_documento, data_formatada, hash_md5, tamanho)
                        cliente.finalizar_envio()
                       
                    case 'LO':
                        cliente.iniciar_sincronismo(protocolo, competencia, cpf, nome, banco, regiao, centro_de_custo, modelo_de_pasta=modelo_de_pasta, label='Diferente')
                        cliente.enviar_partes_do_arquivo(file_name, conteudo_base64)
                        cliente.efetivar_envio(modelo_de_documento, data_formatada, hash_md5, tamanho, modelo_de_pasta=modelo_de_pasta)
                        cliente.finalizar_envio()
                       
                    case 'VA' | 'VT':
                        cliente.iniciar_sincronismo(protocolo, competencia, cpf, nome, banco, regiao, centro_de_custo, modelo_de_pasta=modelo_de_pasta, label='Diferente', pedido=pedido)
                        cliente.enviar_partes_do_arquivo(file_name, conteudo_base64)
                        cliente.efetivar_envio(modelo_de_documento, data_formatada, hash_md5, tamanho, modelo_de_pasta=modelo_de_pasta)
                        cliente.finalizar_envio()
                        
                    case _:
                        cliente.iniciar_sincronismo(protocolo, competencia, cpf, nome, banco, regiao, centro_de_custo)
                        cliente.enviar_partes_do_arquivo(file_name, conteudo_base64)
                        cliente.efetivar_envio(modelo_de_documento, data_formatada, hash_md5, tamanho)
                        cliente.finalizar_envio()
                        
