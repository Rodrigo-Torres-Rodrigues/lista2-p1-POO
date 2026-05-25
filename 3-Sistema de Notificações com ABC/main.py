from domain.centralNotificacoes import CentralNotificacoes
from domain.notificadorEmailAppSMS import *

central1 = CentralNotificacoes()

app1 = NotificadorApp()
sms1 = NotificadorSMS()
email1 = NotificadorEmail()

central1.adicionar_notificador(app1)
central1.adicionar_notificador(sms1)
central1.adicionar_notificador(email1)

central1.enviar_para_todos("Testando 1 2 3")