from domain.boleto import Boleto
from domain.etiqueta import Etiqueta
from domain.relatorioSimples import RelatorioSimples

from services.processarImpressao import processar_impressao

b1 = Boleto("1234a", 12, "Não pode ter cores")
e1 = Etiqueta("Mary Jane", "Rua peter 3", "Precisa ter selo")
r1 = RelatorioSimples("Custos mensais", "Não pode ter meses passados")

processar_impressao(b1)
processar_impressao(e1)
processar_impressao(r1)