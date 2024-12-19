from math import pi

class Forma:
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return pi * (self.raio ** 2)


figuras_geometricas = [Retangulo(10, 15), Quadrado(20), Circulo(13)]

for figura in figuras_geometricas:
    print(f'{figura.calcular_area():.2f}')
