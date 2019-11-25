from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class FornecedorForm(FlaskForm):
    nome_fantasia = StringField('Nome Fantasia', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired('É necessário preencher este campo!'), Length(14, 14, 'O CPNJ não possui um tamanho válido')])
    url = StringField('URL', validators=[DataRequired('É necessário preencher este campo!')])
    submit = SubmitField('Cadastrar')


class FornecedorEditForm(FlaskForm):
    nome_fantasia = StringField('Nome Fantasia', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired(), Length(14, 14, 'O CPNJ não possui um tamanho válido')])
    url = StringField('URL', validators=[DataRequired('É necessário preencher este campo!')])
    edit = SubmitField('Editar')
