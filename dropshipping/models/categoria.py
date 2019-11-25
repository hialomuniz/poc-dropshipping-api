from dropshipping import db
from datetime import datetime


class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(80), index=True, unique=True, nullable=False)
    descricao = db.Column(db.String(200), index=False, unique=False, nullable=False)
    data_criacao = db.Column(db.DateTime, index=False, unique=False, nullable=False, default=datetime.utcnow)

    produtos = db.relationship('Produto', backref='categoria', lazy='dynamic')  # 1-*
