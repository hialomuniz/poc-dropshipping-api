from dropshipping import db


class ProdutoPromocao(db.Model):
    __tablename__ = 'produtopromocao'

    id = db.Column(db.Integer, primary_key=True)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id'))
    id_promocao = db.Column(db.Integer, db.ForeignKey('promocao.id'))

    produtos = db.relationship('Produto', backref=db.backref('produtopromocao', cascade="all, delete-orphan"))
    promocoes = db.relationship('Promocao', backref=db.backref('produtopromocao', cascade="all, delete-orphan"))
