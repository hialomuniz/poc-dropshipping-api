from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from dropshipping import db, login_manager


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    data_criacao = db.Column(db.DateTime, index=False, unique=False, nullable=False, default=datetime.utcnow)
    tipo_usuario = db.Column(db.Boolean, default=False)

    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=True)

    @property
    def password(self):
        raise AttributeError('Não é possível acessar o atributo password')

    @password.setter
    def password(self, senha_texto):
        self.senha = generate_password_hash(senha_texto)

    def verify_password(self, senha_texto):
        return check_password_hash(self.senha, senha_texto)

    def __repr__(self):
        return '<Usuario: {}>'.format(self.email)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
