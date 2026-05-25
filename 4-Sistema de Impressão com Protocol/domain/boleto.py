class Boleto:
    def __init__(self, codigo, valor, requisito):
        self._codigo = codigo
        self._valor = valor
        self._requisito = requisito

    def imprimir(self):
        print(f"Imprimindo boleto...\nBoleto imprimido!\nCusto: {self._valor}")