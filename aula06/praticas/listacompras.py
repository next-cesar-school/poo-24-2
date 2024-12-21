class ListaCompras:
    def __init__(self, nome, data, itens):
        self.nome = nome
        self.data = data
        self.itens = itens
    
    def __add__(self, other):
        nome = self.nome + '_copy'
        data = self.data
        itens = self.itens + other.itens
        return ListaCompras(nome, data, itens)
    
    def __str__(self):
        linhas = []
        linhas.append('*'*20)
        linhas.append('== Lista de Compras ==')
        linhas.append(f'Nome: {self.nome} | Data: {self.data}')
        for item in self.itens:
            linhas.append(f'- {item}')
        linhas.append('*'*20)
        return '\n'.join(linhas)
    
    def __del__(self):
        print(f'{self.nome}, Ai, eu vou morrer....')


feira_da_fruta = ListaCompras('Frutas', '20/12', ['manga', 'maça', 'laranja'])
natal = ListaCompras('Ceia', '25/12', ['Uva Passa', 'Chocotone'])

feira_completa = natal + feira_da_fruta

print(feira_da_fruta)
print(natal)
print(feira_completa)

#del(feira_da_fruta)
