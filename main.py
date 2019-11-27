""" main da aplicação """
import os
import logging

from dropshipping import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


def start_application():
    port = int(os.environ.get('PORT', 5000))

    logging.getLogger(__name__).info('Iniciando aplicação')

    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    start_application()
