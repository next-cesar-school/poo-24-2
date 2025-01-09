import unittest


nome = 'Jader'

def soma(num1: int, num2: int) -> int:
    return num1 + num2

def altera_nome(novo_nome: str) -> None:
    global nome
    nome = novo_nome

def dividir(num1: float, num2: float) -> float:
    if num2 == 0:
        raise ValueError('O segundo valor não pode ser zero!')

    return num1 / num2

class TestSoma(unittest.TestCase):
    def test_soma_simples(self):
        resultado = soma(1, 1)
        self.assertEqual(resultado, 2)

    def test_soma_negativos(self):
        resultado = soma(-10, -5)
        self.assertEqual(resultado, -15)

    def test_alterar_nome(self):
        nome_original = nome
        altera_nome('UmNovoNomeQualquer')
        self.assertNotEqual(nome, nome_original)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)
