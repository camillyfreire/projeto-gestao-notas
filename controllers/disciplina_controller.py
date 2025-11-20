from database.conexao import conectar
from models.disciplina import Disciplina
import psycopg2

def criar_disciplina(nome, professor_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO disciplina (nome, professor_id) VALUES (%s, %s) RETURNING id"
        cursor.execute(sql, (nome, professor_id))
        id_gerado = cursor.fetchone()[0]
        conn.commit()
        return True, f"Disciplina criada com ID {id_gerado}"
    except Exception as e:
        return False, str(e)
    finally:
        if conn: conn.close()

def listar_disciplinas():
    lista = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        # Faz um JOIN para pegar o nome do professor também
        sql = """
            SELECT d.id, d.nome, u.nome 
            FROM disciplina d
            LEFT JOIN usuario u ON d.professor_id = u.id
        """
        cursor.execute(sql)
        for r in cursor.fetchall():
            # r[0]=id, r[1]=nome_disciplina, r[2]=nome_professor
            lista.append({'id': r[0], 'nome': r[1], 'professor': r[2]})
    except Exception as e:
        print(e)
    finally:
        if conn: conn.close()
    return lista