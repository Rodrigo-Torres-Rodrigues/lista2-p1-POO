from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def mostrar_dados(self):
        print(f"Nome do funcionário: {self._nome}\nCPF do funcionário: {self._cpf}")

    @abstractmethod
    def calcular_pagamento(self):
        pass
