import random


def calcula_media(notas: tuple[int]) -> float:
    return sum(notas) / len(notas)

n = (7, 8, 5, 8)
x = ('eita', 'oxe', 'vixe')

print(calcula_media(n))
#print(calcula_media(x))

def buscar_dados(dados: dict[str, int], chave: str) -> int:
    #return dados[chave]
    return dados.get(chave, 0)

fazenda = {'cachorro': 10,
            'vaca': 50,
            'gato': 0}

print(buscar_dados(fazenda, 'vaca'))
print(buscar_dados(fazenda, 'elefante'))

def buscar_usuario(id: int) -> str | None:
    return 'João' if id == 1 else None

nome = 'João'
idade = 0

saida = f"Olá, meu nome é {nome}"
saida += f' e minha idade é {idade} anos.' if idade is not None else '.'

print(saida)

if True:
    print('eita')
