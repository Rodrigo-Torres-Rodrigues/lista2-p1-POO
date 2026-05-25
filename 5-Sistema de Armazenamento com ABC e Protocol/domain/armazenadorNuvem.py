from domain.armazenador import Armazenador

class ArmazenadorNuvem():
    def __init__(self):
        self._listaDadosNuvem = []

    def salvar(self, dado):
        self._listaDadosNuvem.append(dado)
