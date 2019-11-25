from dropshipping import db
from datetime import datetime


class Produto(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(80), index=True, unique=False, nullable=False)
    descricao = db.Column(db.String(200), index=False, unique=False, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    img = db.Column(db.LargeBinary(50000), nullable=False)
    data_criacao = db.Column(db.DateTime, index=False, unique=False, nullable=False, default=datetime.utcnow)

    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    id_fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedor.id'))

    promocoes = db.relationship('Promocao', secondary='produtopromocao')
