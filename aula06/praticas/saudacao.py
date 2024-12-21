class Saudacao:
    def __init__(self, mensagem):
        self.mensagem = mensagem
    
    def __call__(self, nome):
        print(f'{self.mensagem}, {nome}')


felicitacoes = Saudacao('Feliz natal')

felicitacoes('Leônidas')
felicitacoes('Bruno')
