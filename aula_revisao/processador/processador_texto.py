class ProcessadorTexto:
    """Classe que processa linhas de texto de acordo com um modo definido.
    Pode converter para maiúsculo, minúsculo ou fazer outros tratamentos.
    """

    def __init__(self, modo_processo:str):
        """Recebe o modo de processamento. Exemplos: 'upper', 'lower'.
        """

        self.modo_processo = modo_processo
        self.__contador_linha = 0

    def processar(self, linha:str):
        """Processa a linha de acordo com o modo escolhido.
        Retorna a linha transformada.
        """

        if self.modo_processo == 'upper':
            return linha.upper()
        elif self.modo_processo == 'lower':
            return linha.lower()
        elif self.modo_processo == 'strip':
            linha = linha.strip()
            while '  ' in linha:
                linha = linha.replace('  ', ' ')

            return f'{linha}\n'
        elif self.modo_processo == 'list':
            linha = f'{self.__contador_linha} | {linha}'
            self.__contador_linha += 1
            return linha

        return linha
