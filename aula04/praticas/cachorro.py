from animal import Animal


class Cachorro(Animal):
    def latir(self):
        print('Au au')

class Passaro(Animal):
    pass

caco = Cachorro('Caco', 4)
caco.latir()
caco.mover()
print(caco.n_patas)
