import pytest
from libpythonpro_m.spam.enviador_de_email import Enviador
from libpythonpro_m.spam.main import EnviadorDeSpam
from libpythonpro_m.tests.test_spam.test_usuarios import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Mateus', email='mateuslourenco55@outlook.com'),
            Usuario(nome='Rafael', email='mateusalourenco@gmail.com')
        ],
        [
            Usuario(nome='Mateus', email='mateuslourenco55@outlook.com'),
        ]
    ]
)
def test_qde_envio_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mateusalourenco55@outlook.com',
        'Curso Python Pro',
        'Configura os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Mateus', email='mateuslourenco55@outlook.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mateuslourenco@gmail.com',
        'Curso Python Pro',
        'Configura os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'mateuslourenco@gmail.com',
        'mateuslourenco55@outlook.com',
        'Curso Python Pro',
        'Configura os módulos fantásticos'
    )
