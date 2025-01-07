
try:
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira outro número: '))

    resultado = n1 / n2
except ValueError:
    print('Não foi possível converter uma ou várias entradas!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
else:
    print(resultado)
finally:
    print('Fim do programa.')
