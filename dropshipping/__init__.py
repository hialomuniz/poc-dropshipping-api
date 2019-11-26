""" init da aplicação """
import os
import logging
import logging.config

from pathlib import Path

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()

from dropshipping.models.categoria import Categoria
from dropshipping.models.cidade import Cidade
from dropshipping.models.endereco import Endereco
from dropshipping.models.fornecedor import Fornecedor
from dropshipping.models.pessoa import Pessoa
from dropshipping.models.produto import Produto
from dropshipping.models.promocao import Promocao
from dropshipping.models.tabela_associacao import ProdutoPromocao
from dropshipping.models.usuario import Usuario

from dropshipping.admin import admin
from dropshipping.auth import auth
from dropshipping.home import home


def create_app(config_name):
    log_config_path = os.path.join(Path(__file__).parent.absolute(), 'log/logger.conf')

    if not (os.path.isfile(log_config_path)):
        assert os.environ.get('LOG_FILE'), 'É necessário informar o path do arquivo de configuração do log!'

        log_config_path = os.environ.get('LOG_FILE')

    logging.config.fileConfig(log_config_path)

    logging.getLogger(__name__).info('Criando objeto da aplicação')

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "Você precisa estar logado para acessar esta página!"
    login_manager.login_view = "auth.login"

    Bootstrap(app)
    migrate = Migrate(app, db)

    logging.getLogger(__name__).info('Registrando blueprints')

    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth)
    app.register_blueprint(home)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Acesso proibido'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Página não encontrada'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Erro genérico'), 500

    return app
