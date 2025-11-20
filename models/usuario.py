
from werkzeug.security import generate_password_hash, check_password_hash
from models.enums import Perfil

class Usuario:
    def __init__(self, nome: str, email: str, perfil: Perfil, id: int = None, senha_hash: str = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.perfil = perfil
        self.senha_hash = senha_hash # O hash será salvo aqui quando buscarmos do DB

    def set_senha(self, senha: str):
        self.senha_hash = generate_password_hash(senha, method='pbkdf2:sha256')

    def check_senha(self, senha: str) -> bool:
        if self.senha_hash is None:
            return False
        return check_password_hash(self.senha_hash, senha)

    def __str__(self):
        return f"Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', perfil='{self.perfil.value}')"

    # Validações (como no projeto anterior)
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or len(valor) < 3:
            raise ValueError("Nome muito curto!")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ValueError("E-mail inválido. Deve conter '@' e '.'")
        self._email = valor