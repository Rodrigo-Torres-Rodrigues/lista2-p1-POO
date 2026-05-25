from domain.funcionario import Funcionario

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, cpf, total_vendas, percentual_comissao):
        super().__init__(nome, cpf)
        self._total_vendas = total_vendas
        self._percentual_comissao = percentual_comissao

    def calcular_pagamento(self):
        print(f"Pagamento de {self._nome}:", self._total_vendas * self._percentual_comissao)