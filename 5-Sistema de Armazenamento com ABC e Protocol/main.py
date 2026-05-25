from domain.armazenadorArquivo import ArmazenadorArquivo
from domain.armazenadorBanco import ArmazenadorBanco
from domain.armazenadorNuvem import ArmazenadorNuvem

from services.executar_salvamento_flexivel import executar_salvamento_flexivel
from services.executar_salvamento_formal import executar_salvamento_formal

a1 = ArmazenadorArquivo()
b1 = ArmazenadorBanco()
n1 = ArmazenadorNuvem()

executar_salvamento_formal(a1, "*dado importante*")
executar_salvamento_formal(b1, "*dado importante*")
executar_salvamento_formal(n1, "*dado importante*")

executar_salvamento_flexivel(a1, "*dado importante*")
executar_salvamento_flexivel(b1, "*dado importante*")
executar_salvamento_flexivel(n1, "*dado importante*")