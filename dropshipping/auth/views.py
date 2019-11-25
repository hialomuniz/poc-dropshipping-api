from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from dropshipping.auth import auth
from dropshipping.auth.forms import LoginForm
from dropshipping.models.usuario import Usuario


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        # if usuario is not None and usuario.verify_password(form.password.data):
        if usuario is not None:
            login_user(usuario)

            return redirect(url_for('home.dashboard'))
        else:
            flash('E-mail ou senha inválidos!')

    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    flash('Logout efetuado com sucesso!')

    return redirect(url_for('auth.login'))
