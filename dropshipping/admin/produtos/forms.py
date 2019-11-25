from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, FileField
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class ProdutoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired('É necessário preencher este campo!'), Length(max=80, message='Máximo de 80 caracteres')])
    descricao = StringField('Descrição', validators=[DataRequired('É necessário preencher este campo!'),
                                                     Length(max=200, message='Máximo de 200 caracteres')])
    preco = DecimalField('Preço (R$)', places=2)
    quantidade = IntegerField('Quantidade')
    imagem = FileField('Imagem')
    categoria = SelectField('Categoria', coerce=int)
    fornecedor = SelectField('Fornecedor', coerce=int)

    submit = SubmitField('Cadastrar')


class ProdutoEditForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired('É necessário preencher este campo!'), Length(max=80, message='Máximo de 80 caracteres')])
    descricao = StringField('Descrição', validators=[DataRequired('É necessário preencher este campo!'),
                                                     Length(max=200, message='Máximo de 200 caracteres')])
    preco = DecimalField('Preço (R$)', places=2)
    quantidade = IntegerField('Quantidade')
    imagem = FileField('Imagem')
    categoria = SelectField('Categoria', coerce=int)
    fornecedor = SelectField('Fornecedor', coerce=int)

    edit = SubmitField('Editar')
