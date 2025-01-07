class Pessoa():
    def __init__(self, nome: str, email: str, endereço: str):
        self.nome: str = nome
        self.email: str = email
        self.endereco: str = endereço
        self.habilidades: list[str] = []

    def adicionar_habilidade(self, habilidade: str) -> None:
        if habilidade not in self.habilidades:
            self.habilidades.append(habilidade)

    def listar_habilidades(self) -> list[str]:
        return self.habilidades

    def __str__(self) -> str:
        habilidades = ', '.join(self.habilidades) if self.habilidades \
            else 'Nenhuma habilidade cadastrada'
        return f'Pessoa: {self.nome} | Habilidades: {habilidades}'

if __name__ == '__main__':
    pessoa1 = Pessoa('Pedro', 'peu@cesar.shcool', 'Rua da Jogatina')
    pessoa1.adicionar_habilidade('Programação')
    pessoa1.adicionar_habilidade('Design')
    print(pessoa1.listar_habilidades())
