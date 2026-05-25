class Empresa:
    def __init__(self, nome):
        self._nome = nome
        self._lista_funcionarios = []

    def adicionar_funcioanario(self, funcionarioNovo):
        self._lista_funcionarios.append(funcionarioNovo)

    def listar_funcionarios(self):
        for funcionario in self._lista_funcionarios:
            funcionario.mostrar_dados()

    def mostrar_folha_pagamento(self):
        for funcionario in self._lista_funcionarios:
            funcionario.calcular_pagamento()