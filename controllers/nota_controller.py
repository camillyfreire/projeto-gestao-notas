from database.conexao import conectar
import psycopg2

def lancar_nota(aluno_id, disciplina_id, descricao, valor):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = """
            INSERT INTO nota (aluno_id, disciplina_id, descricao, valor) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (aluno_id, disciplina_id, descricao, valor))
        conn.commit()
        return True, "Nota lançada com sucesso!"
    except Exception as e:
        return False, str(e)
    finally:
        if conn: conn.close()

def listar_notas_por_aluno(aluno_id):
    lista = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = """
            SELECT n.descricao, d.nome, n.valor, n.data_lancamento
            FROM nota n
            JOIN disciplina d ON n.disciplina_id = d.id
            WHERE n.aluno_id = %s
        """
        cursor.execute(sql, (aluno_id,))
        for r in cursor.fetchall():
            lista.append({
                'descricao': r[0],
                'disciplina': r[1],
                'valor': r[2],
                'data': r[3]
            })
    except Exception as e:
        print(e)
    finally:
        if conn: conn.close()
    return lista