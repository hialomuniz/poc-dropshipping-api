from dropshipping import db
from datetime import datetime


class Promocao(db.Model):
    __tablename__ = 'promocao'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(80), index=True, unique=False, nullable=False)
    descricao = db.Column(db.String(200), index=False, unique=False, nullable=False)
    data_criacao = db.Column(db.DateTime, index=False, unique=False, nullable=False, default=datetime.utcnow)
    data_inicio = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    data_fim = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)

    produtos = db.relationship('Produto', secondary='produtopromocao')
