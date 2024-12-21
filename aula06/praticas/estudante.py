class Estudante:
    def __init__(self):
        self.__notas = []
        self.__nota_atual = 0
    
    def add_notas(self, nota):
        if len(self.__notas) < 4:
            self.__notas.append(nota)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__nota_atual < 4:
            nota = self.__notas[self.__nota_atual]
            self.__nota_atual += 1
            return nota
        else:
            raise StopIteration


fulano = Estudante()

fulano.add_notas(10)
fulano.add_notas(8)
fulano.add_notas(7)
fulano.add_notas(3)
fulano.add_notas(9)

for nota in fulano:
    print(nota)
