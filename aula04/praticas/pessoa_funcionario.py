class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        self.cargo = cargo
        super().__init__(nome, idade)

isabella = Funcionario('Isabella', 27, 'Dev Junior')

print(isabella.nome)
print(isabella.idade)
print(isabella.cargo)
