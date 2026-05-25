class Plataforma:
    def __init__(self, nome):
        self._nome = nome
        self._listaMidia = []

    def adicionar_midia(self, midia):
        self._listaMidia.append(midia)

    def listar_midia(self):
        for midia in self._listaMidia:
            midia.mostrar_info()

    def reproduzir_todas(self):
        for midia in self._listaMidia:
            midia.reproduzir()