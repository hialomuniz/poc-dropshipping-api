from flask import render_template, abort
from flask_login import login_required, current_user

from . import home


@home.route('/')
def homepage():
    return render_template('home/index.html', title="Página inicial")


@home.route('/admin/dashboard')
@login_required
def dashboard():
    if not current_user.tipo_usuario:
        abort(403)

    return render_template('home/dashboard.html', title="Página principal")
