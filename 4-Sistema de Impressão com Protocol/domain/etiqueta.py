class Etiqueta:
    def __init__(self, destinatario, endereco, requisito):
        self._destinatario = destinatario
        self._endereco = endereco
        self._requisito = requisito

    def imprimir(self):
        print(f"Imprimindo estiqueta com destinatário: {self._destinatario} com o endereço: {self._endereco}")