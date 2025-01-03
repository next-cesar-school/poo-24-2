def soma(a: int, b: int) -> int:
    return a + b

print(soma(10, 5))
print(soma('Eita', 'Oxe'))
print(soma(10.5, 8.12))

class Estudante():
    def __init__(self, nota: float) -> None:
        self.nota = nota

def avaliar_estudante(pessoa: Estudante) -> None:
    if pessoa.nota >= 7:
        print('Aprovado')
    else:
        print('Reprovado')

dante = Estudante(9.9)
pedro = Estudante(2.7)

avaliar_estudante(dante)
avaliar_estudante(pedro)
