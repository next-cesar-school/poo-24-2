class Playlist:
    def __init__(self, nome, musicas):
        self.nome = nome
        self.musicas = musicas
    
    def __len__(self):
        return len(self.musicas)


pedrada = Playlist('Só Pedrada', ['m1', 'm2', 'm3'])

print(len(pedrada))
