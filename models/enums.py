from enum import Enum

class Perfil(Enum):
    ADMIN = 'ADMIN'
    PROFESSOR = 'PROFESSOR'
    ALUNO = 'ALUNO'

    @staticmethod
    def listar_perfis():
        return [perfil.value for perfil in Perfil]