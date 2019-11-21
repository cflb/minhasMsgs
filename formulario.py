from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class CadastroUsuarioForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao = SubmitField('Cadastrar')

class MensagemForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    botao = SubmitField('Enviar MSG')