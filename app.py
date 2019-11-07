from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nova-mensagem')
def novaMensagem():
    return render_template('mensagens.html')


if __name__ == "__main__":
    app.run(debug=True)

