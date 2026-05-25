from domain.notificador import Notificador

class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        print(f"Nova mensagem no seu Email: {mensagem}")
    
class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        print(f"Nova mensagem no seu SMS: {mensagem}")
    
class NotificadorApp(Notificador):
    def notificar(self, mensagem):
        print(f"Nova mensagem do aplicativo: {mensagem}")