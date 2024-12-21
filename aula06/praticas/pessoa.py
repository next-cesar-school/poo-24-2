class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.id = 10
        self.cod = 12345
    
    def exibir_detalhes(self):
        pass

    def __str__(self):
        return f'Esta é uma instância da Classe Pessoa\n\tNome: {self.nome} e \tIdade: {self.idade}\n'

    def __repr__(self):
        return f'Pessoa(nome=\'{self.nome}\', idade={self.idade}, id={self.id}, cod={self.cod})'


caio = Pessoa('Caio Santana', 26)
caio.nome = 'Dawsley Santana'

print(caio)
print(repr(caio))
