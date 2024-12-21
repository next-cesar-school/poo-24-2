class Tabela:
    def __init__(self):
        self.dados = {}
        #self.dados = []
        #self.dados = ''
    
    def __setitem__(self, chave, valor):
        self.dados[chave] = valor
        #self.dados.append(tuple([chave, valor]))
        #self.dados += f'{chave}🦙{valor}🥐'
    
    def __getitem__(self, chave):
        return self.dados[chave]

informacoes = Tabela()
informacoes['Aracelly'] = 'Matriculada'
informacoes['Manuel'] = 'Formado'

print(informacoes['Manuel'])
#print(informacoes.dados)
