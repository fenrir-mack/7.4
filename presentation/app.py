import sys
import os

# Ajuste para permitir importações das outras camadas a partir da raiz (tarefa4_clean)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for, flash
from use_cases.livro_usecase import LivroUseCase
from infrastructure.txt_repository import TxtLivroRepository

app = Flask(__name__, template_folder='templates')
app.secret_key = 'chave_secreta_para_flash_messages'

# Injeção de Dependência (Composition Root)
db_path = os.path.join(os.path.dirname(__file__), '..', 'infrastructure', 'banco.txt')
repository = TxtLivroRepository(filepath=db_path)
livro_usecase = LivroUseCase(repository)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = livro_usecase.obter_todos_livros()

    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "filtrar":
            tipo = request.form.get("tipo")
            valor = request.form.get("valor")
            if tipo and valor:
                resultado = livro_usecase.filtrar_livros(tipo, valor)
        
        elif acao == "adicionar":
            titulo = request.form.get("titulo")
            autor = request.form.get("autor")
            categoria = request.form.get("categoria")
            editora = request.form.get("editora")
            
            sucesso, msg = livro_usecase.adicionar_livro(titulo, autor, editora, categoria)
            flash(msg)
            return redirect(url_for("index"))

    return render_template("index.html", livros=resultado)

if __name__ == "__main__":
    app.run(debug=True)
