class Animal:
    def emitir_som(self):
        print('Emitindo um som genérico')

class Cachorro(Animal):
    def emitir_som(self):
        print('Au Au')

class Passaro(Animal):
    def emitir_som(self):
        print('bem-te-vi')
    
    def voar(self):
        print('Voa minha liberdade!')

class Ornitorrinco(Animal):
    pass


if __name__ == '__main__':
    def fazer_falar(animal_qualquer):
        animal_qualquer.emitir_som()
        print(type(animal_qualquer))

    bicho = Animal()
    rex = Cachorro()
    bem_te_vi = Passaro()
    perry = Ornitorrinco()

    arca = [bicho, rex, bem_te_vi, perry]

    for animal in arca:
        fazer_falar(animal)

    '''fazer_falar(bicho)
    fazer_falar(rex)
    fazer_falar(bem_te_vi)
    fazer_falar(perry)'''
