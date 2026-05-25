from domain.armazenador import Armazenador

class ArmazenadorBanco(Armazenador):
    def __init__(self):
        self._listaDadosBanco = []

    def salvar(self, dado):
        self._listaDadosBanco.append(dado)