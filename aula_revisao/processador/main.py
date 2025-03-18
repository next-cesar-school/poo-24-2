from processador_texto import ProcessadorTexto


caminho = 'aula_revisao/processador/'

def main():
    modo = input('Digite o modo de processamento do texto (upper|lower|strip|list): ')
    entrada = input('Digite o nome do arquivo de entrada: ')
    saida = input('Digite o nome do arquivo de saída: ')

    processador = ProcessadorTexto(modo)

    with open(caminho + entrada, encoding='utf-8') as arq_entrada, \
        open(caminho + saida, 'w', encoding='utf-8') as arq_saida:
            for linha in arq_entrada:
                linha_processada = processador.processar(linha)
                arq_saida.write(linha_processada)

    print('Programa encerrado.')


if __name__ == '__main__':
    main()
