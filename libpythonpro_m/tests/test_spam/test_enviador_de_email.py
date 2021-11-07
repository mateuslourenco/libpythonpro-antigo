import pytest

from libpythonpro_m.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['mateuslourenco55@outlook.com', 'karpen1977@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        '%s' % remetente,
        'mateuslalourenco@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Carlos Leite'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'karpen1977']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            '%s' % remetente,
            'mateuslalourenco@gmail.com',
            'Cursos Python Pro',
            'Primeira turma Carlos Leite'
        )
