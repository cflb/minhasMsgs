from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


from formulario import MensagemForm, CadastroUsuarioForm

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhasmensagens.db'
app.config['SECRET_KEY'] = 'lsrhvanlvlqtaçcojgq'

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(10), unique=False, nullable=False)
    mensagem = db.relationship('Mensagem', backref='usuario', lazy=True)

    def __repre__(self):
        return '[User: %r]' % self.login

class Mensagem(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(
        db.Integer, 
        db.ForeignKey('usuario.id'), 
        nullable=False
    ) 

    def __repre__(self):
        return self.mensagem

















@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():

    form = CadastroUsuarioForm()
    print(form.login.data)
    print(form.email.data)
    print(form.senha.data)

    if form.validate_on_submit():
        user1 = Usuario()
        user1.login = form.login.data
        user1.email = form.email.data
        user1.senha = form.senha.data
        db.session.add(user1)
        db.session.commit()
    
    
    """
        user1 = Usuario()

        In [5]: user1.login = 'joao'

        In [6]: user1.email = 'joao@iai.io'

        In [7]: user1.senha = '123qwe123'

        In [8]: db.session.add(user1)

        In [9]: db.session.commit()
    """
    return render_template('cadastro.html', form=form)





@app.route('/')
def index():

    
    return render_template('index.html')


@app.route('/nova-mensagem', methods=['GET','POST'])
def novaMensagem():
    

    form = MensagemForm()

    if form.validate_on_submit():
        msg = Mensagem()
        msg.usuario_id = 1 #temporaria - apenas envia para o user de id 1
        msg.titulo = form.titulo.data
        msg.mensagem = form.mensagem.data
        db.session.add(msg)
        db.session.commit()


    return render_template('mensagens.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)