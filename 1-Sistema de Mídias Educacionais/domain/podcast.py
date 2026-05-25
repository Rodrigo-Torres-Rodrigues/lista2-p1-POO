from domain.midia import Midia

class Podcast(Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)
        self._apresentador = apresentador

    def reproduzir(self):
        print(f"Fala galera! estamos aqui para mais um Podcast!!!")