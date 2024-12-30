import requests


class E2DocClient:

    def __init__(self):
        self.usuario = "**************"
        self.senha = "********"
        self.keybase = "EQS"
        self.file_name = None
        self.protocolo = None
        self.token = None
        

    def autenticar(self):
        url = "https://www.e2doc.com.br/e2doc_api/Autentica/Usuario"
        parametros = {
            "keybase": self.keybase,
            "Usuario": self.usuario,
            "Senha": self.senha,
            "Modulo": "sincronismo",
            "Param": "",
            "Versao": 20
        }
        response = requests.post(url, json=parametros)
        if response.status_code == 200:
            self.token = response.json().get("AccessToken")
        else:
            return "Conexão não estabelecida entre os sistemas"



    def iniciar_sincronismo(self, protocolo, competencia, cpf, nome, banco, regiao, centro_de_custo, modelo_de_pasta="FINANCEIRO - DP", label='Comum', pedido=""):
        """
        Sincroniza a automação com o sistema E2DOC.
        Além de preencher préviamente o formulário da pasta modelo.

        Retorna:
            "Sincronismo iniciado" se a comunicação for bem-sucedida.
        Lança:
            Exception: Se ocorrer um erro durante a sincronização.
        """

        if label != 'Comum':
            indices = [
                {"label": "COMPETÊNCIA", "valor": competencia},
                {"label": "CPF", "valor": cpf},
                {"label": "NOME DO FUNCIONARIO", "valor": nome},
                {"label": "PEDIDO", "valor": pedido},
                {"label": "BANCO", "valor": banco},
                {"label": "SINDICATO", "valor": ""},
                {"label": "CENTRO DE CUSTO", "valor": centro_de_custo}
            ]
        else:
            indices = [
                {"label": "COMPETÊNCIA", "valor": competencia},
                {"label": "CPF", "valor": cpf},
                {"label": "NOME DO FUNCIONARIO", "valor": nome},
                {"label": "PEDIDO", "valor": pedido},
                {"label": "BANCO", "valor": banco},
                {"label": "SINDICATO", "valor": ""},
                {"label": "ESTADO", "valor": ""},
                {"label": "REGIÃO", "valor": regiao},
                {"label": "CENTRO DE CUSTO", "valor": centro_de_custo}
            ]

        self.protocolo = protocolo
        url = 'https://www.e2doc.com.br/e2doc_api/Sincronismo/Iniciar'
        parametros = {
            "token": self.token,
            "usuario": self.usuario,
            "protocolo": self.protocolo,
            "modeloPasta": modelo_de_pasta,
            "indices": indices
        }
        response = requests.post(url, json=parametros)
        if response.status_code == 200:
            print("Sincronismo iniciado")
        else:
            raise Exception("Erro ao iniciar sincronismo:", response.status_code, response.text)



    def enviar_partes_do_arquivo(self, file_name, arquivo):
        """
        Envia o arquivo préviamente para o E2DOC.
        Dá a opção de enviar o arquivo fracionado em partes caso ele seja muito pesado.
        Ou, em caso de um arquivo simples (como são os arquivos lançados por essa automação),
        é através deste mesmo método que eles também serão enviados.

        Retorna:
            "Arquivo simples enviado com sucesso!" se o envio for bem-sucedido.
        Lança:
            Exception: Se ocorrer um erro durante o envio.
        """

        self.file_name = file_name
        url = f"https://www.e2doc.com.br/e2doc_api/Sincronismo/EnviarParte"
        parametros = {
            "token": self.token,
            "fileNamePart": self.file_name,
            "buffer": arquivo
        }
        response = requests.post(url, json=parametros)
        
        if response.status_code == 200:
            print(f"Arquivo simples enviado com sucesso!")
        else:
            raise Exception(f"Erro ao enviar arquivo: {response.status_code}, {response.text}")



    def efetivar_envio(self, modelo_de_documento, data, hash_md5, tamanho, modelo_de_pasta="FINANCEIRO - DP"):
        """
        Efetiva o envio do arquivo para a plataforma E2DOC,
        além de preencher alguns outros campos do formulário da pasta modelo FINANCEIRO - DP.
        O envio do documento para o E2DOC através da API é feito em duas etapas:
        Primeiro enviamos partes do arquivo (caso seja necessário) através da função "/Sincronismo/EnviarParte";
        Segundo, efetivamos o envio do arquivo em sua totalidade com todos os metadados necessários preenchidos,
        através da função "/Sincronismo/EnviarArquivo".

        Retorna:
            "Documento enviado com sucesso!" se o envio for bem-sucedido.
        Lança:
            Exception: Se ocorrer um erro durante o envio.
        """

        url = "https://www.e2doc.com.br/e2doc_api/Sincronismo/EnviarArquivo"
        parametros = {
            "token": self.token,
            "Documento": {
                "modeloDocumento": modelo_de_documento,
                "descricao": modelo_de_documento,
                "usuario": self.usuario,
                "data": data,
                "partes": [self.file_name],
                "path": "",
                "hash": hash_md5,
                "extensao": ".pdf",
                "tamanho": tamanho,
                "paginas": 1,
                "sequencia": 1,
                "versiona": 0
            },
            "ModeloPasta": modelo_de_pasta,
            "protocolo": self.protocolo
        }
        response = requests.post(url, json=parametros)
        if response.status_code == 200:
            print("Documento enviado com sucesso!")
        else:
            raise Exception("Erro ao enviar o documento:", response.status_code, response.text)



    def finalizar_envio(self):
        """
        Finaliza o processo de enviar um documento para a plataforma E2DOC através da API.

        Retorna:
            "Processo finalizado. Documento integrado à plataforma." se a finalização for bem-sucedida.
        Lança:
            Exception: Se ocorrer um erro durante o encerramento do processo.
        """

        url = "https://www.e2doc.com.br/e2doc_api/Sincronismo/Finalizar"
        parametros = {
            "token": self.token,
            "protocolo": self.protocolo,
            "flags": ""
        }
        response = requests.post(url, json=parametros)
        if response.status_code == 200:
            print("Processo finalizado. Documento integrado à plataforma.")
        else:
            raise Exception("Erro ao finalizar processo:", response.status_code, response.text)

