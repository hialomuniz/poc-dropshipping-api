
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class FornecedorForm(FlaskForm):
    nome_fantasia = StringField('Nome Fantasia', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired(), Length(14, 14, 'O CPNJ não possui um tamanho válido')])
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
