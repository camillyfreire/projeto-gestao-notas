from decimal import Decimal

class Nota:
    def __init__(self, aluno_id: int, disciplina_id: int, descricao: str, valor: Decimal, id: int = None):
        self.id = id
        self.aluno_id = aluno_id
        self.disciplina_id = disciplina_id
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return (f"Nota(id={self.id}, aluno_id={self.aluno_id}, disciplina_id={self.disciplina_id}, "
                f"descricao='{self.descricao}', valor={self.valor})")