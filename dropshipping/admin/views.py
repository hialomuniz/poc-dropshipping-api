from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from dropshipping.admin import admin
from dropshipping.admin.forms import FornecedorForm
from dropshipping import db
from dropshipping.models.fornecedor import Fornecedor


def check_admin():
    if not current_user.tipo_usuario:
        abort(403)


@admin.route('/fornecedores', methods=['GET', 'POST'])
@login_required
def list_fornecedores():
    check_admin()

    fornecedores = Fornecedor.query.all()

    return render_template('admin/fornecedores/fornecedores.html', fornecedores=fornecedores, title="Fornecedores")


@admin.route('/fornecedores/add', methods=['GET', 'POST'])
@login_required
def add_fornecedor():
    check_admin()

    form = FornecedorForm()

    if form.validate_on_submit():
        fornecedor = Fornecedor(nome_fantasia=form.nome_fantasia.data,
                                cnpj=form.cnpj.data,
                                url=form.url.data)
        try:
            db.session.add(fornecedor)
            db.session.commit()

            flash('Fornecedor adicionado com sucesso!')
        except:
            flash('Erro ao adicionar fornecedor!')

        return redirect(url_for('admin.list_fornecedores'))

    return render_template('admin/fornecedores/add.html',
                           action="Add",
                           form=form,
                           title="Adicionar fornecedor")


@admin.route('/fornecedores/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_fornecedor(id):
    check_admin()

    fornecedor = Fornecedor.query.get_or_404(id)

    form = FornecedorForm(obj=fornecedor)

    if form.validate_on_submit():
        fornecedor.nome_fantasia = form.nome_fantasia.data
        fornecedor.cnpj = form.cnpj.data
        fornecedor.url = form.url.data

        db.session.commit()
        flash('Fornecedor editado com sucesso!')

        return redirect(url_for('admin.list_fornecedores'))

    #  form.description.data = department.description
    #  form.name.data = department.name
    return render_template('admin/fornecedores/edit.html',
                           action="Edit",
                           form=form,
                           fornecedor=fornecedor,
                           title="Editar fornecedor")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    check_admin()

    fornecedor = Fornecedor.query.get_or_404(id)

    db.session.delete(fornecedor)
    db.session.commit()

    flash('Fornecedor deletado com sucesso')

    return redirect(url_for('admin.list_fornecedores'))

    return render_template(title="Deletar fornecedor")
