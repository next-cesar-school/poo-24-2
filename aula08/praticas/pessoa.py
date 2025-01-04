"""Módulo Pessoa que possui a classe pessoa do sistema."""

class Pessoa:
    """Representa uma pessoa no sistema.

    Atributos:
        nome (str): Nome completo da pessoa.
        idade (int): Idade em anos da pessoa.
    
    Métodos:
        saudacao(): Retorna uma saudação da pessoa.
    """

    def __init__(self, nome: str, idade: int) -> None:
        """Inicializa uma instância de Pessoa.
        
        Parâmetros:
            nome (str): Nome completo da pessoa.
            idade (int): Idade em anos da pessoa.
        """
        self.nome = nome
        self.idade = idade

    def saudacao(self) -> str:
        """Retorna uma saudação, citando seu próprio nome.

        Retorna:
            str: Saudação com seu próprio nome.
        """

        return f'Ola, meu nome é {self.nome}'

joao = Pessoa('João da Silva', 25)
