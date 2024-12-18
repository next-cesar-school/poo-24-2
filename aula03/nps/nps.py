class NPS:
    def __init__(self):
        self.__notas = []
    
    '''def get_notas(self):
        return self.__notas'''

    def adicionar_notas(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print('Nota inválida!\nInsira uma nota entre 0 e 10!')

    def calcular_nps(self):
        # descobrir a quantidade de detratores e promotores
        detratores = len([n for n in self.__notas if n < 7])
        promotores = len([n for n in self.__notas if n >= 9])

        # calcular o % de detratores e promotores
        percentual_detratores = (detratores / len(self.__notas)) * 100
        percentual_promotores = (promotores / len(self.__notas)) * 100

        # calcula o NPS
        nps = percentual_promotores - percentual_detratores
        return nps
    
    def exibir_classificacao(self):
        nps = self.calcular_nps()
        print(f'NPS: {nps}')
        if nps >= 75:
            print('Zona de Excelência')
        elif nps >= 50:
            print('Zona de Qualidade')
        elif nps >= 0:
            print('Zona Neutra')
        else:
            print('Zona Crítica')


if __name__ == '__main__':
    avaliacao = NPS()

    avaliacao.adicionar_notas(10)
    avaliacao.adicionar_notas(8)
    avaliacao.adicionar_notas(7)
    avaliacao.adicionar_notas(9)
    avaliacao.adicionar_notas(5)
    avaliacao.adicionar_notas(7)
    avaliacao.adicionar_notas(3)
    avaliacao.adicionar_notas(-5)
    avaliacao.adicionar_notas(0)
    avaliacao.adicionar_notas(9)
    avaliacao.adicionar_notas(10)
    avaliacao.adicionar_notas(10)
    avaliacao.adicionar_notas(9)
    avaliacao.adicionar_notas(9)
    avaliacao.adicionar_notas(10)

    #avaliacao.__notas.append(10)

    print(avaliacao.calcular_nps())
    avaliacao.exibir_classificacao()
