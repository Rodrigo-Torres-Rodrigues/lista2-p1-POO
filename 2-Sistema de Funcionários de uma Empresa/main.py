from domain.empresa import Empresa
from domain.funcionarioAssalariado import FuncionarioAssalariado
from domain.funcionarioComissionado import FuncionarioComissionado
from domain.funcionarioHorista import FuncionarioHorista

emp1 = Empresa("Youtube")

f1 = FuncionarioAssalariado("José", "000.000.000-00", "2750")
h1 = FuncionarioHorista("Maria", "000.000.000-00", 8, 12.5)
c1 = FuncionarioComissionado("Elizabeth", "000.000.000-00", 41, 10)

emp1.adicionar_funcioanario(f1)
emp1.adicionar_funcioanario(h1)
emp1.adicionar_funcioanario(c1)

emp1.listar_funcionarios()

emp1.mostrar_folha_pagamento()