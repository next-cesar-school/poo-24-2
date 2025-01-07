class ContaBancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError('O valor de deposito precisa ser maior que zero.')

        self.__saldo += valor

    def sacar(self, valor: float) -> None:
        if valor > self.__saldo:
            raise SaldoInsuficienteError(self.__saldo, valor)

        self.__saldo -= valor

    def get_saldo(self) -> str:
        return self.__saldo

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo: float, valor: float) -> None:
        super().__init__(f'Saldo Insuficiente. Saldo atual: R$ {saldo:.2f}, Valor a ser debitado: R$ {valor:.2f}')

if __name__ == '__main__':
    try:
        jader = ContaBancaria('Jader Lima', 10000.0)
        jader.depositar(1000)
        #jader.depositar(-500)
        print(jader.get_saldo())
        jader.sacar(4000)
        #jader.sacar(50000)
        print(jader.get_saldo())
    except ValueError as ve:
        print(ve)
    except SaldoInsuficienteError as sie:
        print(sie)
