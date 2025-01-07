"""
Representação e teste de um jogo.
"""

class Jogo():
    """Classe que representa um jogo digital da FORJA"""

    def __init__(self, nome: str, sinopse: str, genero: str, estagio: str) -> None:
        self.nome = nome
        self.sinopse = sinopse
        self.gero = genero
        self.estagio = estagio
        self.__ativo = True

    def set_ativo(self, ativo:bool) -> None:
        """Define o status de atividade do jogo.
        - `True` se o projeto estiver ativo.
        - `False` se o projeto não estiver ativo"""
        self.__ativo = ativo

    def is_ativo(self) -> bool:
        """Retorna verdadeiro se o projeto estiver ativo"""
        return self.__ativo

    def __str__(self)  -> str:
        return f'Jogo: {self.nome} | Estágio: {self.estagio} | '\
            f'{'Ativo' if self.__ativo else 'Desativado'}'

if __name__ == '__main__':
    j1 = Jogo('Helena', 'Jogo de terror sobre a emparedada da rua nova', 'Terror', 'Em Produção')

    print(j1.nome)
    print(j1.sinopse)
    j1.set_ativo(False)
    print(j1.is_ativo())
