"""Módulo principal para processamento de dados de entrada e geração de saída.

Este módulo lê um arquivo CSV contendo informações de pessoas, instancia objetos da classe `Pessoa`
e gera um novo arquivo CSV filtrando registros com status diferente de 'cancelled'.
"""

from pessoa import Pessoa


def main():
    lista_pessoas = []

    with open('aula_revisao/email/dados_entrada.csv', encoding='utf-8') as arquivo:
        for linha in arquivo.readlines()[1:]:
            nome_completo, _, codigo, status = linha.split(',')
            pessoa = Pessoa(nome_completo, codigo, status, lista_pessoas)
            lista_pessoas.append(pessoa)

    with open('saida_nomes.csv', mode='w', encoding='utf-8') as file:
        file.write('nome,sobrenome,email,codigo\n')

        for pessoa in lista_pessoas:
            if pessoa.status != 'cancelled':
                file.write(f'{pessoa.primeiro_nome},{pessoa.segundo_nome},'
                        f'{pessoa.email_institucional},{pessoa.codigo}\n')

if __name__ == '__main__':
    main()
