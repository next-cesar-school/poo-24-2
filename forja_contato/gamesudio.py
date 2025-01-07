"""
Representação de um Game Studio da FORJA
"""


from jogo import Jogo


class GameStudio():
    "Entidade Game Studio"

    def __init__(self, nome: str, link: str) -> None:
        self.nome = nome
        self.link = link
        self.__jogos: list[Jogo] = []
        self.__ativo = True

    def set_ativo(self, ativo:bool) -> None:
        """Define o status de atividade do Game Studio.

        - `True` se o projeto estiver ativo.
        - `False` se o projeto não estiver ativo
        """

        self.__ativo = ativo

    def is_ativo(self) -> bool:
        """Retorna verdadeiro se o projeto estiver ativo"""
        return self.__ativo

    def add_jogo(self, jogo:Jogo) -> None:
        """Adiciona um novo jogo ao Game Studio"""

        self.__jogos.append(jogo)

    def listar_jogos(self) -> None:
        """Exibe o nome de todos os jogos do Game Studio"""

        for jogo in self.__jogos:
            print(f'- {jogo.nome} | {'Ativo' if jogo.is_ativo() else 'Desativado'}')

    def get_jogo(self, nome_jogo: str) -> Jogo:
        """Retorna um jogo pelo nome"""

        for jogo in self.__jogos:
            if nome_jogo.lower() == jogo.nome.lower():
                return jogo


if __name__ == '__main__':

    gs1 = GameStudio('GVG', 'goodvillagegames.com')
    gs1.set_ativo(False)

    isekaid = Jogo('Isekaid', 'Veja diferentes mundos', 'Roguelike', 'Pré produção')
    gs1.add_jogo(isekaid)

    pts = Jogo('Punch! Throw!! Score!!!', 'Batalha lendária', 'Arcade', 'Produção')
    gs1.add_jogo(pts)

    gs1.listar_jogos()
    isekaid = gs1.get_jogo('Isekaid')
    isekaid.set_ativo(False)

    print(isekaid)
