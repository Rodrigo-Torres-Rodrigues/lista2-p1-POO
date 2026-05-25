from domain.plataforma import Plataforma
from domain.video import Video
from domain.podcast import Podcast
from domain.textoNarrado import TextoNarrado

ecampus = Plataforma("ecampus")

v1 = Video("A queda de roma", 35, "1440x768")
p1 = Podcast("A história da África", 126, "João Silva")
t1 = TextoNarrado("ww2", 35, "Portugues")

ecampus.adicionar_midia(v1)
ecampus.adicionar_midia(p1)
ecampus.adicionar_midia(t1)

ecampus.listar_midia()

ecampus.reproduzir_todas()