"""Validador de CPF"""


class CPFInvalidoError(Exception):
    """Representa um erro de CPF inválido"""

    def __init__(self, cpf):
        super().__init__(f"O CPF {cpf} é inválido.")


class CPF:
    """Representa um CPF - Cadastro de Pessoa Física"""

    def __init__(self, cpf: str) -> None:
        self.__cpf = ''.join(filter(str.isdigit, cpf))

        if len(self.__cpf) != 11:
            raise CPFInvalidoError(cpf)

    def validar(self) -> bool:
        """Verifica se o CPF é válido
        
        Retorna `True` se o CPF for válido.  
        """

        if len(set(self.__cpf)) == 1:
            return False  # CPFs com todos os dígitos iguais são inválidos.

        # Cálculo do primeiro dígito verificador
        soma = sum(int(self.__cpf[i]) * (10 - i) for i in range(9))

        digito1 = (soma * 10) % 11

        if digito1 == 10:
            digito1 = 0

        # Cálculo do segundo dígito verificador
        soma = sum(int(self.__cpf[i]) * (11 - i) for i in range(10))

        digito2 = (soma * 10) % 11

        if digito2 == 10:
            digito2 = 0

        return self.__cpf[-2:] == f"{digito1}{digito2}"

    def __str__(self) -> str:
        return f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}"


# Teste
if __name__ == '__main__':
    try:
        meu_cpf = CPF("529.982.247-25")

        print(f"CPF {meu_cpf} é válido? {meu_cpf.validar()}")
    except CPFInvalidoError as e:
        print(e)
