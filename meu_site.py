from flask import Flask

app = Flask(__name__)


@app.route('/home')
def homepage():
    # retornar a imagem "segue_o_lider.png" da pasta "static"
    return "<img src='/static/segue_o_lider.png'>"

@app.route("/contatos")
def contatos():
    return "Esses são os meus contatos"

if __name__ == "__main__":
    app.run(debug=True)
