class SaldoInsuficienteError(Exception):
    def __init__(self, saldo: float, valor: float) -> None:
        super().__init__(f'Saldo Insuficiente. Saldo atual: R$ {saldo:.2f}, Valor a ser debitado: R$ {valor:.2f}')

def sacar(saldo: float, valor: float) -> float:
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)

    if valor >= 3000:
        raise ValueError('Valor muito grande!')

    saldo -= valor

    return saldo


if __name__ == '__main__':
    try:
        valor_final = sacar(3000.0, 5000.00)
        print(f'R$ {valor_final:.2f}')
    except SaldoInsuficienteError as liso:
        print(liso)
        print('Não é possível debitar mais do que você tem na conta, bocó! Quer ficar individado, é?')
