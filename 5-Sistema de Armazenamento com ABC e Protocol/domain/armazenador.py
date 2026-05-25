from abc import ABC, abstractmethod

class Armazenador(ABC):
    @abstractmethod
    def salvar(dado):
        pass