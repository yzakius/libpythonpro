from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador)
    enviador_de_spam.enviar_emails(
        'isaac@isaac.com',
        'Aprendendo Testes',
        'Lets Go!',
    )
