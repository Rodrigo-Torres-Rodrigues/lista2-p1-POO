class RelatorioSimples:
    def __init__(self, titulo, requisito):
        self._titulo = titulo
        self._requisito = requisito

    def imprimir(self):
        print(f"Imprimindo o relatório '{self._titulo}'")