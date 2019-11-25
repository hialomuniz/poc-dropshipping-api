from dropshipping import db


class Endereco(db.Model):
    __tablename__ = 'endereco'

    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(80), index=False, unique=False, nullable=False)
    numero = db.Column(db.String(20), index=False, unique=False, nullable=False)
    complemento = db.Column(db.String(80), index=False, unique=False, nullable=True)
    bairro = db.Column(db.String(80), index=False, unique=False, nullable=False)
    cep = db.Column(db.String(10), index=False, unique=False, nullable=False)

    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id'))

    pessoa = db.relationship('Pessoa', uselist=False, backref='endereco')
