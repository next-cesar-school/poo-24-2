def calcular_media(valores: list[int]) -> float:
    """Calcula a média de uma lista de valores inteiros.

    Parâmetros:
        valores (list[int]): Lista de notas da prova.
    
    Retorna:
        float: Média aritmética dos valores.
    """

    return sum(valores) / len(valores)

calcular_media([1, 2, 3, 4, 5])
