from libpythonpro_m.spam.enviador_de_email import Enviador
from libpythonpro_m.spam.main import EnviadorDeSpam


def test_qde_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'mateusalourenco55@outlook.com',
        'Curso Python Pro',
        'Configura os módulos fantásticos'
    )
