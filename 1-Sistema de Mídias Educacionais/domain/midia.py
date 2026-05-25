from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo, duracao):
        self._titulo = titulo
        self._duracao = duracao

    def mostrar_info(self):
        print(f"Título: {self._titulo}\nDuracação: {self._duracao}")

    @abstractmethod
    def reproduzir(self):
        pass