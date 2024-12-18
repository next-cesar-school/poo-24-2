class Animal:
    def __init__(self, nome, n_patas):
        self.nome = nome
        self.n_patas = n_patas

    def mover(self):
        print(f'O {self.nome} está se movendo')

if __name__ == '__main__':
    bichinho = Animal('Triago', 3)
    bichinho.latir()
