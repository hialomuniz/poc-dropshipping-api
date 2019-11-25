from flask import redirect, render_template, url_for, abort
from flask_login import login_required, current_user

from . import home


@home.route('/')
def homepage():
    if current_user.is_authenticated and current_user.tipo_usuario:
        return redirect(url_for('home.dashboard'))

    return render_template('home/index.html', title="Página inicial")


@home.route('/admin/dashboard')
@login_required
def dashboard():
    if not current_user.tipo_usuario:
        abort(403)

    return render_template('home/dashboard.html', title="Página principal")
