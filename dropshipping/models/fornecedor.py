from dropshipping import db
from datetime import datetime


class Fornecedor(db.Model):
    __tablename__ = 'fornecedor'

    id = db.Column(db.Integer, primary_key=True)

    nome_fantasia = db.Column(db.String(80), index=True, unique=False, nullable=False)
    cnpj = db.Column(db.String(14), index=True, unique=True, nullable=False)
    url = db.Column(db.String(100), index=False, unique=False, nullable=False)
    data_criacao = db.Column(db.DateTime, index=False, unique=False, nullable=False, default=datetime.utcnow)
    ativo = db.Column(db.Boolean, default=True)

    produtos = db.relationship('Produto', backref='fornecedor', lazy='dynamic')
