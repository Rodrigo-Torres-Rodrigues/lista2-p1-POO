from typing import Protocol

class Salvavel(Protocol):
    def salvar(dado) -> None:
        ...