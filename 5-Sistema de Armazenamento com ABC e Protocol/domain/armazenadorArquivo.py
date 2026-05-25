from domain.armazenador import Armazenador

class ArmazenadorArquivo(Armazenador):
    def __init__(self):
        self._listaDadosArq = []

    def salvar(self, dado):
        self._listaDadosArq.append(dado)