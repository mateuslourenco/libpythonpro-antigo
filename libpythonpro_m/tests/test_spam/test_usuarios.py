class Sesssao:
    contador = 0
    usuarios = []

    def salvar(self, usuario):
        Sesssao.contador += 1
        usuario.id = Sesssao.contador
        self.usuarios.append(usuario)

    def listar(self):
        return self.usuarios

    def rollback(self):
        self.usuarios.clear()

    def fechar(self):
        pass


class Conexao:
    def gerar_sessao(self):
        return Sesssao()

    def fechar(self):
        pass


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Mateus')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.rollback()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Mateus'), Usuario(nome='Mateus')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.rollback()
    sessao.fechar()
    conexao.fechar()
