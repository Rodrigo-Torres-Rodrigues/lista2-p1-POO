from domain.midia import Midia

class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self._resolucao = resolucao

    def reproduzir(self):
        print(f"Vídeo carregando...\nVídeo Rodando!")