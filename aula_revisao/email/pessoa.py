"""Módulo que define a classe `Pessoa`, responsável pelo gerenciamento de nomes e e-mails."""


class Pessoa:
    """Classe que representa uma pessoa e realiza manipulações em seus dados.
    
    Ela também separa corretamente o primeiro e o segundo nome, tratando preposições e criando
    um e-mail institucional único.
    """

    preposicoes = ('da', 'do', 'de', 'dos', 'das')

    def __init__(self, nome_completo:str, codigo:str, status:str, lista_pessoas:list):
        self.nome_completo = nome_completo
        self.codigo = codigo
        self.status = status

        self.__nome_sobrenome()
        self.__criar_email_institucional(lista_pessoas)

    def __repr__(self):
        return self.nome_completo

    def __nome_sobrenome(self):
        nome_separado = self.nome_completo.split()

        self.primeiro_nome = nome_separado[0].capitalize()

        self.segundo_nome = nome_separado[1].capitalize()

        # verifica se o segundo nome é um conectivo
        if self.segundo_nome.lower() in Pessoa.preposicoes:
            self.segundo_nome = nome_separado[2].capitalize()
            #self.segundo_nome = f'{self.segundo_nome.lower()} {nome_separado[2].capitalize()}'

        print(self.primeiro_nome, self.segundo_nome)

    def __criar_email_institucional(self, lista_pessoas):
        nome_separado = self.nome_completo.split()

        # pegar as iniciais sem os conectivos
        email = ''
        for nome in nome_separado:
            if nome.lower() not in Pessoa.preposicoes:
                email += nome[0].lower()

        # checar se esse email já existe
        for pessoa in lista_pessoas:
            if email+'@zecar.school' == pessoa.email_institucional:
                email = self.__email_existente(email, pessoa.email_institucional)

        self.email_institucional = f'{email}@zecar.school'

    def __email_existente(self, email_nome:str, email_encontrado:str):
        numero = ''.join([num for num in email_encontrado if num.isdigit()])

        if numero == '':
            # retornar número com um 2
            return f'{email_nome}2'
        else:
            # retornar o número como número + 1
            return email_nome.replace(numero, f'{int(numero) + 1}')
