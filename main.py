from views.menu import menu_principal
import sys

# Garante que o console aceite caracteres UTF-8 (acentos)
sys.stdout.reconfigure(encoding='utf-8')

if __name__ == "__main__":
    # Inicia o programa chamando o menu principal
    menu_principal()