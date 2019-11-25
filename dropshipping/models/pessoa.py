from dropshipping import db


class Pessoa(db.Model):
    __tablename__ = 'pessoa'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), index=True, unique=False, nullable=False)
    cpf = db.Column(db.String(11), index=True, unique=True, nullable=False)
    data_nascimento = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    sexo = db.Column(db.String(1), index=False, unique=False, nullable=False)

    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))

    usuario = db.relationship('Usuario', uselist=False, backref='pessoa')
