from controllers.usuario_controller import criar_usuario, listar_usuarios, login_usuario
from models.usuario import Usuario
from models.enums import Perfil
import getpass # Para esconder a senha

def menu_principal():
    """
    Menu interativo para testar o backend de usuários.
    """
    while True:
        print("\n--- GESTÃO DE NOTAS (TESTE DE BACKEND) ---")
        print("1 - Criar Novo Usuário")
        print("2 - Listar Usuários")
        print("3 - Fazer Login")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            _menu_criar_usuario()
        
        elif opcao == "2":
            _menu_listar_usuarios()

        elif opcao == "3":
            _menu_login()

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def _menu_criar_usuario():
    print("\n--- Criar Novo Usuário ---")
    try:
        nome = input("Nome: ")
        email = input("Email: ")
        
        # Senha Segura
        senha = getpass.getpass("Senha: ") 
        senha_conf = getpass.getpass("Confirme a Senha: ")

        if senha != senha_conf:
            print("As senhas não conferem!")
            return

        print("Perfis disponíveis:", Perfil.listar_perfis())
        perfil_input = input("Perfil (ALUNO, PROFESSOR, ADMIN): ").upper()
        
        perfil = Perfil(perfil_input) 
        
        novo_usuario = Usuario(nome=nome, email=email, perfil=perfil)
        novo_usuario.set_senha(senha)
        criar_usuario(novo_usuario)

    except ValueError as e:
        print(f"Erro: {e}") 
    except Exception as e:
        print(f"Erro inesperado ao criar usuário: {e}")

def _menu_listar_usuarios():
    print("\n--- Listar Usuários ---")
    usuarios = listar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in usuarios:
            print(u)
def _menu_login():
    print("\n--- Login ---")
    try:
        email = input("Email: ")
        senha = getpass.getpass("Senha: ")
        
        usuario_logado = login_usuario(email, senha)
        
        if usuario_logado:
            print(f"Acesso liberado para: {usuario_logado}")
        else:
            print("Acesso negado.")
            
    except Exception as e:
        print(f"Erro inesperado ao fazer login: {e}")