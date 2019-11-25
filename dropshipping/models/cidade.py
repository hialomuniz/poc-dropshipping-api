from dropshipping import db


class Cidade(db.Model):
    __tablename__ = 'cidade'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, unique=True, nullable=False)
    estado = db.Column(db.String(20), index=False, unique=False, nullable=False)
    endereco = db.relationship('Endereco', uselist=False, backref='cidade')
