from unittest.mock import Mock

import pytest
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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mateusalourenco55@outlook.com',
        'Curso Python Pro',
        'Configura os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Mateus', email='mateuslourenco55@outlook.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mateuslourenco@gmail.com',
        'Curso Python Pro',
        'Configura os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'mateuslourenco@gmail.com',
        'mateuslourenco55@outlook.com',
        'Curso Python Pro',
        'Configura os módulos fantásticos'
    )
