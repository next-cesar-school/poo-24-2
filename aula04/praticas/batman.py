class Mamifero:
    def amamentar(self):
        print('Amamentando...')

class Ave:
    def voar(self):
        print('Voando...')

class Morcego(Mamifero, Ave):
    def sonar(self):
        print('Vendo tudo mesmo no escuro Tu tu tu tu tu tu')

guto = Morcego()

guto.amamentar()
#guto.voar()
#guto.sonar()
