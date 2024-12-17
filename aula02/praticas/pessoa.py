class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0
    
    def set_idade(self, idade):
        if idade >= 0:
            self.idade = idade
        else:
            print(f'🙅‍♂️ Não é possível inserir uma idade negativa para a pessoa {self.nome}')
    
    def get_idade(self):
        return f'{self.idade} anos'


igor = Pessoa('Igor Nicholai')
jailton = Pessoa('JAIlton Valeriano')

igor.set_idade(28)
jailton.set_idade(-10)
jailton.set_idade(20)

print(igor.nome)
print(igor.get_idade())

print(jailton.nome)
print(jailton.get_idade())
