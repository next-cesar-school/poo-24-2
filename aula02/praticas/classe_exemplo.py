class Carro:
    n_rodas = 4
    
    def __init__(self, modelo_carro, potencia_motor, step):
        self.modelo = modelo_carro
        self.motor = potencia_motor
        self.tem_step = step
    
    def exibir_detalhes(self):
        print(f'Carro com {self.n_rodas} rodas e modelo {self.modelo} tem um motor {self.motor} e sobre o step: {self.tem_step}')


sentra = Carro('sedan', 2.0, True)
fox = Carro('hatch', 1.0, False)

sentra.exibir_detalhes()
fox.exibir_detalhes()

modelo = input('Insira o modelo do carro: ')
motor = float(input('Qual a potência do motor desse carro? '))
step = input('Esse carro tem step?').lower() == 'sim'

carro1 = Carro(modelo, motor, step)
carro1.exibir_detalhes()

'''print(sentra.n_rodas)
print(sentra.modelo)
print(sentra.motor)
print(sentra.tem_step)

print(fox.n_rodas)
print(fox.modelo)
print(fox.motor)
print(fox.tem_step)'''
