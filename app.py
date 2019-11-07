from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from formulario import MensagemForm

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhasmensagens.db'
app.config['SECRET_KEY'] = 'lsrhvanlvlqtaçcojgq'

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)

    def __repre__(self):
        return self.mensagem

@app.route('/')
def index():

    msgs = Mensagem.query.all()


    return render_template('index.html', msgs=msgs)

@app.route('/nova-mensagem', methods=['POST', 'GET'])
def novaMensagem():
    form = MensagemForm()
    if form.validate_on_submit():
        msg = Mensagem()
        msg.mensagem = form.mensagem.data
        db.session.add(msg)
        db.session.commit()

    return render_template('mensagens.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)