import requests
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'chave_secreta_cliente'

SERVER_URL = 'https://8ponto4-a0dwchavdjdyd8f4.brazilsouth-01.azurewebsites.net/'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "adicionar":
            dados = {
                "titulo": request.form.get("titulo"),
                "autor": request.form.get("autor"),
                "categoria": request.form.get("categoria"),
                "editora": request.form.get("editora"),
            }
            response = requests.post(f"{SERVER_URL}/livros", json=dados)
            result = response.json()
            flash(result.get("mensagem") or result.get("erro"))
            return redirect(url_for("index"))

        elif acao == "filtrar":
            tipo = request.form.get("tipo")
            valor = request.form.get("valor")
            response = requests.get(f"{SERVER_URL}/livros/filtrar", params={"tipo": tipo, "valor": valor})
            livros = response.json()
            return render_template("index.html", livros=livros)

    # GET padrão - carrega todos os livros
    response = requests.get(f"{SERVER_URL}/livros")
    livros = response.json()
    return render_template("index.html", livros=livros)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
