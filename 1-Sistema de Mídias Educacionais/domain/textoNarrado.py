from domain.midia import Midia

class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self._idioma = idioma

    def reproduzir(self):
        print(f"*Texto sendo falado por uma voz robótica*")