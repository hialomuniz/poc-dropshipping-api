""" init da aplicação """
from flask import Flask
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
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    Bootstrap(app)
    migrate = Migrate(app, db)

    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth)
    app.register_blueprint(home)

    return app


"""
import os
import logging

from flask import Flask
from flasgger import Swagger


def create_app():

    Função responsável por setar o objeto da aplicação.



    log_config_path = os.path.join(Path(__file__).parent.absolute(), 'log/logger.conf')

    if not (os.path.isfile(log_config_path)):
        assert os.environ.get('LOG_FILE'), 'É necessário informar o path do arquivo de configuração do log!'

        log_config_path = os.environ.get('LOG_FILE')

    app.config['zxing'] = True

    template = {
        'swagger': '2.0',
        'info': {
            'title': 'API de Código de Barras',
            'description': 'Documentação das APIs de identificação/leitura de código de barras',
            'version': __version__
        },
        "termsOfService": '',
    }

    logging.config.fileConfig(log_config_path)

    logging.getLogger(__name__).info('Criando objeto da aplicação')

    Swagger(app, template=template)

    app.register_blueprint(INDEX)
    app.register_blueprint(ERROR)
    app.register_blueprint(METRICS)
    app.register_blueprint(IMAGE_READER, url_prefix='/api/v1')
    app.register_blueprint(PDF_READER, url_prefix='/api/v1')

    app = Flask(__name__)

    return app
    """
