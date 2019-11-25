from flask import Blueprint

home = Blueprint('home', __name__)

from dropshipping.home import views
