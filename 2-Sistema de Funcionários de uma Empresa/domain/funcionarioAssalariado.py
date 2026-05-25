from domain.funcionario import Funcionario

class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, cpf, salario_mensal):
        super().__init__(nome, cpf)
        self._salario_mensal = salario_mensal

    def calcular_pagamento(self):
        print(f"Pagamento de {self._nome}:", self._salario_mensal)