from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhasmensagens.db'

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)

    def __repre__(self):
        return self.mensagem



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nova-mensagem')
def novaMensagem():
    return render_template('mensagens.html')


if __name__ == "__main__":
    app.run(debug=True)

