from enum import Enum

class Perfil(Enum):
    ADMIN = 'ADMIN'
    PROFESSOR = 'PROFESSOR'
    ALUNO = 'ALUNO'

    # Esta função é útil para listar as opções no menu
    @staticmethod
    def listar_perfis():
        return [perfil.value for perfil in Perfil]