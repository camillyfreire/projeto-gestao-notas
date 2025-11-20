from flask import Flask, render_template, request, redirect, url_for, session, flash
from controllers.usuario_controller import login_usuario, criar_usuario, listar_usuarios
from controllers.disciplina_controller import criar_disciplina, listar_disciplinas
from controllers.nota_controller import lancar_nota, listar_notas_por_aluno
from models.usuario import Usuario
from models.enums import Perfil

app = Flask(__name__)
app.secret_key = 'chave_super_secreta_para_sessao' # Necessário para login funcionar

# --- ROTA INICIAL (LOGIN) ---
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        usuario = login_usuario(email, senha)
        
        if usuario:
            # Salva dados na sessão do navegador
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['usuario_perfil'] = usuario.perfil.value
            return redirect(url_for('dashboard'))
        else:
            flash('Email ou senha incorretos!')
            
    return render_template('login.html')

# --- DASHBOARD (MENU PRINCIPAL) ---
@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# --- LOGOUT ---
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# --- CADASTROS (SÓ ADMIN) ---
@app.route('/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    if session.get('usuario_perfil') != 'ADMIN':
        flash('Acesso negado!')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        perfil_str = request.form['perfil']
        
        novo_user = Usuario(nome, email, Perfil(perfil_str))
        novo_user.set_senha(senha)
        criar_usuario(novo_user)
        flash('Usuário cadastrado com sucesso!')
        
    return render_template('cadastro_usuario.html', perfis=Perfil.listar_perfis()) # Precisaremos criar esse HTML

@app.route('/cadastro_disciplina', methods=['GET', 'POST'])
def cadastro_disciplina():
    if session.get('usuario_perfil') != 'ADMIN':
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        nome = request.form['nome']
        prof_id = request.form['professor_id']
        ok, msg = criar_disciplina(nome, prof_id)
        flash(msg)

    professores = [u for u in listar_usuarios() if u.perfil == Perfil.PROFESSOR]
    return render_template('cadastro_disciplina.html', professores=professores) # Criar HTML

# --- NOTAS ---
@app.route('/lancar_notas', methods=['GET', 'POST'])
def lancar_notas():
    if session.get('usuario_perfil') != 'PROFESSOR':
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        aluno_id = request.form['aluno_id']
        disc_id = request.form['disciplina_id']
        desc = request.form['descricao']
        valor = request.form['valor']
        ok, msg = lancar_nota(aluno_id, disc_id, desc, valor)
        flash(msg)

    alunos = [u for u in listar_usuarios() if u.perfil == Perfil.ALUNO]
    disciplinas = listar_disciplinas()
    return render_template('lancar_notas.html', alunos=alunos, disciplinas=disciplinas) # Criar HTML

@app.route('/meu_boletim')
def meu_boletim():
    # Se for aluno, vê só as suas. Se for prof/admin, poderia ver de todos (simplificado aqui)
    notas = listar_notas_por_aluno(session['usuario_id'])
    return render_template('boletim.html', notas=notas) # Criar HTML

if __name__ == '__main__':
    app.run(debug=True)