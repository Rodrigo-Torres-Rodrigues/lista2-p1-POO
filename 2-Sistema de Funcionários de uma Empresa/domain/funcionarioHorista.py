from domain.funcionario import Funcionario

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, cpf, horas_trabalhadas, valor_hora):
        super().__init__(nome, cpf)
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora

    def calcular_pagamento(self):
        print(f"Pagamento de {self._nome}:", self._horas_trabalhadas * self._valor_hora)