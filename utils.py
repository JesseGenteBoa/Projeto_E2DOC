import os
import base64
import hashlib
import smtplib
from email.message import EmailMessage



def retornar_mes(mes):
    meses = {
        '01': 'JANEIRO',
        '02': 'FEVEREIRO',
        '03': 'MARÇO',
        '04': 'ABRIL',
        '05': 'MAIO',
        '06': 'JUNHO',
        '07': 'JULHO',
        '08': 'AGOSTO',
        '09': 'SETEMBRO',
        '10': 'OUTUBRO',
        '11': 'NOVEMBRO',
        '12': 'DEZEMBRO' 
    }
    return f'{mes} - {meses[mes]}'



def retornar_banco(caminho):
    match caminho:
        case _ if "ITAU" in caminho:
            banco = "ITAU"
        case _ if "SANTANDER" in caminho:
            banco = "SANTANDER"
        case _ if "BRADESCO" in caminho:
            banco = "BRADESCO"
        case _ if "CEF" in caminho:
            banco = "CEF"
        case _ if "BB" in caminho:
            banco = "BB (BANCO DO BRASIL)"
    return banco



def criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='Simples', pedido=''):
    if 'RESCISOES' in diretorio_destino:
        ano_vigente = f'RESCISAO {ano_vigente}'

    if not ano_vigente in os.listdir(diretorio_destino):
        os.mkdir(diretorio_destino + "\\" + ano_vigente)

    diretorio_destino = diretorio_destino + "\\" + ano_vigente

    if not mes_vigente in os.listdir(diretorio_destino):
        os.mkdir(diretorio_destino + "\\" + mes_vigente)

    diretorio_destino = diretorio_destino + "\\" + mes_vigente

    if '13 SALARIO' not in tipo:
        if not data_de_pagamento in os.listdir(diretorio_destino):
            os.mkdir(diretorio_destino + "\\" + data_de_pagamento)
        
        diretorio_destino = diretorio_destino + "\\" + data_de_pagamento

    if tipo != 'Simples':
        if pedido != '':
            tipo = tipo + " - " + pedido
            if not tipo in os.listdir(diretorio_destino):
                os.mkdir(diretorio_destino + "\\" + tipo)

        elif tipo in ['1ª 13 SALARIO', '2ª 13 SALARIO', 'TJ 13 SALARIO']:
            if 'TJ' in tipo:
                tipo = 'TRIBUNAL DE JUSTIÇA'
            else:    
                tipo = f'{tipo[:2]} PARCELA {data_de_pagamento}'
            if not tipo in os.listdir(diretorio_destino):
                os.mkdir(diretorio_destino + "\\" + tipo)

        elif tipo == '13 SALARIO':
            tipo = ""

        elif not tipo in os.listdir(diretorio_destino):
            os.mkdir(diretorio_destino + "\\" + tipo)

        diretorio_destino = diretorio_destino + "\\" + tipo

    return diretorio_destino



def enviar_email(relatorio, data_festiva):
    match data_festiva:
        case "01/04":
            feriado = '''Viva à fantasia, a capacidade humana de imaginar e contar a realidade como ela deveria ser!\n"Não sei, só sei que foi assim" - Chicó'''
        case _ if "15/04" <= data_festiva <= "20/04":
            feriado = "E que venham os chocolates!"
        case "01/05":
            feriado = "Feliz dia do trabalhador para você que trabalha e sente muita dor."
        case "11/05":
            feriado = "Feliz dia das mães!"
        case "12/06":
            feriado = "Para todos os sortudos que encontraram o amor, Feliz dia dos namorados!"
        case "10/08":
            feriado = "Feliz dia dos pais!"
        case "07/09":
            feriado = "Viva a nossa independência!"
        case "12/10":
            feriado = "Feliz dia das nossas crianças!"
        case "02/11":
            feriado = "Saudemos os nossos mortos. Eles estão diante do maior mistério da nossa existência, o estar ou o não estar."
        case _ if "20/12" <= data_festiva <= "31/12":
            feriado = "Boas festas!"
        case _:
            feriado = ""

    list_tratada = ["".join(lista) for lista in relatorio]
    string = "\n".join(list_tratada)

    corpo = f'''
Olá, colaborador!

Segue um relatório do que foi enviado pela automação para o E2DOC;


Envios totais: {len(relatorio)}

Processos enviados:

NOME  -  MODELO DE DOCUMENTO  -  COMPETENCIA

{string}



{feriado}

Grato pela colaboração.

Atensiosamente,
Doc Hudson,

    '''

    carta = EmailMessage()
    carta.set_content(corpo)
    carta['Subject'] = "Enviados para o E2DOC"
    carta['From'] = "eqsengenharia@eqsengenharia.com.br"
    carta['To'] = "Financeiro@eqsengenharia.com.br"

    try:
        with smtplib.SMTP_SSL('grid331.mailgrid.com.br', 465) as servidor:
            servidor.login("eqsengenharia@eqsengenharia.com.br", "YXPLlbnL2N")
            servidor.send_message(carta)
    except Exception as e:
        pass



def ler_arquivo(caminho):
    tamanho = os.path.getsize(caminho)

    with open(caminho, 'rb') as arquivo:
        conteudo = arquivo.read()
        conteudo_base64 = base64.b64encode(conteudo).decode("utf-8")
        md5_hash = hashlib.md5(conteudo).hexdigest().upper()

    return conteudo_base64, md5_hash, tamanho



def zerar_lista_controle(lista_controle):
    while not lista_controle.empty():
        lista_controle.get()
        lista_controle.task_done()
