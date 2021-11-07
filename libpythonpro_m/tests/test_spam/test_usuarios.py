import pytest


class Sessao:
    contador = 0
    usuarios = []

    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def listar(self):
        return self.usuarios

    def rollback(self):
        self.usuarios.clear()

    def fechar(self):
        pass


class Conexao:
    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None


@pytest.fixture
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield Conexao()
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.rollback()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Mateus')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Mateus'), Usuario(nome='Mateus')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
