from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CategoriaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired('É necessário preencher este campo!'), Length(max=80, message='Máximo de 80 caracteres')])
    descricao = StringField('Descrição', validators=[DataRequired('É necessário preencher este campo!'),
                                                     Length(max=200, message='Máximo de 200 caracteres')])

    submit = SubmitField('Cadastrar')


class CategoriaEditForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired('É necessário preencher este campo!'), Length(max=80, message='Máximo de 80 caracteres')])
    descricao = StringField('Descrição', validators=[DataRequired('É necessário preencher este campo!'),
                                                     Length(max=200, message='Máximo de 200 caracteres')])

    edit = SubmitField('Editar')
