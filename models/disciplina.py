class Disciplina:
    def __init__(self, nome: str, professor_id: int = None, id: int = None):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id

    def __str__(self):
        return f"Disciplina(id={self.id}, nome='{self.nome}', professor_id={self.professor_id})"