""" main da aplicação """
import os

from dropshipping import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    app.run()

"""
import os
import logging

from dropshipping import create_app

APP = create_app()


def start_application():
    port = int(os.environ.get('PORT', 5001))

    logging.getLogger(__name__).info('Iniciando aplicação')

    APP.run(host='0.0.0.0', port=port, debug=False)


if __name__ == '__main__':
    start_application()
"""
