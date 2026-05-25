class CentralNotificacoes:
    def __init__(self):
        self._lista_notificacao = []

    def adicionar_notificador(self, notificador):
        self._lista_notificacao.append(notificador)

    def enviar_para_todos(self, mensagem):
        for notificador in self._lista_notificacao:
            notificador.notificar(mensagem)