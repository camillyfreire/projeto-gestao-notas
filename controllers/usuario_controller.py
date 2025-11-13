from database.conexao import conectar
from models.usuario import Usuario
from models.enums import Perfil
import psycopg2

def criar_usuario(usuario: Usuario):
    """
    Cria um novo usuário no banco de dados.
    A senha DEVE ser definida (hashed) no objeto Usuario ANTES de chamar esta função.
    """
    try:
        conn = conectar()
        if conn is None:
            raise Exception("Não foi possível conectar ao banco.")
            
        cursor = conn.cursor()
        
        if usuario.senha_hash is None:
            raise ValueError("A senha não foi definida para o usuário.")
            
        sql = """
        INSERT INTO usuario (nome, email, senha_hash, perfil) 
        VALUES (%s, %s, %s, %s) 
        RETURNING id
        """
        
        cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha_hash, usuario.perfil.value))
        
        usuario.id = cursor.fetchone()[0] # Recupera o ID gerado
        
        conn.commit()
        print(f"Usuário criado com sucesso: {usuario}")
        
    except psycopg2.Error as e:
        print(f"Erro ao criar usuário: {e}")
        if conn:
            conn.rollback() # Desfaz a transação em caso de erro
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def listar_usuarios():
    """
    Lista todos os usuários do banco de dados.
    """
    usuarios = []
    try:
        conn = conectar()
        if conn is None:
            raise Exception("Não foi possível conectar ao banco.")
            
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email, perfil FROM usuario")
        resultados = cursor.fetchall()
        
        for r in resultados:
            perfil_enum = Perfil(r[3]) 
            usuario = Usuario(id=r[0], nome=r[1], email=r[2], perfil=perfil_enum)
            usuarios.append(usuario)
            
    except psycopg2.Error as e:
        print(f"Erro ao listar usuários: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
    return usuarios

def login_usuario(email: str, senha: str) -> Usuario | None:
    """
    Tenta autenticar um usuário.
    Retorna o objeto Usuario se o login for bem-sucedido, None caso contrário.
    """
    try:
        conn = conectar()
        if conn is None:
            raise Exception("Não foi possível conectar ao banco.")
            
        cursor = conn.cursor()
        
        sql = "SELECT id, nome, email, perfil, senha_hash FROM usuario WHERE email = %s"
        cursor.execute(sql, (email,))
        
        resultado = cursor.fetchone()
        
        if resultado:
            id_db, nome_db, email_db, perfil_db, senha_hash_db = resultado
            
            perfil_enum = Perfil(perfil_db)
            usuario_logando = Usuario(id=id_db, nome=nome_db, email=email_db, 
                                      perfil=perfil_enum, senha_hash=senha_hash_db)
            
            if usuario_logando.check_senha(senha):
                print(f"Login bem-sucedido! Bem-vindo(a), {usuario_logando.nome}.")
                return usuario_logando # Sucesso!
            else:
                print("Senha incorreta.")
                return None # Senha errada
        else:
            print("Usuário não encontrado.")
            return None # Email não encontrado
            
    except psycopg2.Error as e:
        print(f"Erro ao tentar login: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
    return None