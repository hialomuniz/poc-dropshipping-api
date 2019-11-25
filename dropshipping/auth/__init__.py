from flask import Blueprint

auth = Blueprint('auth', __name__)

from dropshipping.auth import views  # TODO: verificar o import circular que está quebrando a aplicação quando coloca este import na parte superior
