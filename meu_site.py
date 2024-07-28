from flask import Flask

app = Flask(__name__)


@app.route('/home')
def homepage():
    return "Essa é minha HomePage"

@app.route("/contatos")
def contatos():
    return "Esses são os meus contatos"

app.run()