from nps import NPS


def rodar_pesquisa():
    pesquisa = NPS()

    while True:
        nota = int(input('Insira sua avaliação de 0 a 10\nInsira um valor negativo para sair: '))

        if nota < 0:
            break

        pesquisa.adicionar_notas(nota)

    #pesquisa.notas.append('eita, que nota boa!')
    #pesquisa.notas.append('é 10 pai')

    #pesquisa.__notas.append(-10)
    #pesquisa.__notas.append(-8)
    #pesquisa.__notas.append(-7)

    pesquisa.exibir_classificacao()

def dar_oi(nome):
    print(f'Oi, {nome}')

if __name__ == '__main__':
    rodar_pesquisa()
