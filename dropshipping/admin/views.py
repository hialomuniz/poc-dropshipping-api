from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from dropshipping import db
from dropshipping.admin import admin
from dropshipping.admin.fornecedores.forms import FornecedorForm, FornecedorEditForm
from dropshipping.admin.produtos.forms import ProdutoForm, ProdutoEditForm
from dropshipping.admin.categorias.forms import CategoriaForm, CategoriaEditForm

from dropshipping.models.fornecedor import Fornecedor
from dropshipping.models.produto import Produto
from dropshipping.models.categoria import Categoria


def check_admin():
    if not current_user.tipo_usuario:
        abort(403)


"""
Rotas para cadastro de fornecedores
"""
@admin.route('/fornecedores', methods=['GET', 'POST'])
@login_required
def list_fornecedores():
    check_admin()

    fornecedores = Fornecedor.query.all()

    return render_template('admin/fornecedores/list.html', fornecedores=fornecedores, title="Fornecedores")


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
                           form=form,
                           title="Adicionar fornecedor")


@admin.route('/fornecedores/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_fornecedor(id):
    check_admin()

    fornecedor = Fornecedor.query.get_or_404(id)

    form = FornecedorEditForm(obj=fornecedor)

    if form.validate_on_submit():
        fornecedor.nome_fantasia = form.nome_fantasia.data
        fornecedor.cnpj = form.cnpj.data
        fornecedor.url = form.url.data
        fornecedor.ativo = True if form.ativo.data == 1 else False

        db.session.commit()
        flash('Fornecedor editado com sucesso!')

        return redirect(url_for('admin.list_fornecedores'))

    return render_template('admin/fornecedores/edit.html',
                           form=form,
                           fornecedor=fornecedor,
                           title="Editar fornecedor")


@admin.route('/fornecedores/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_fornecedor(id):
    check_admin()

    fornecedor = Fornecedor.query.get_or_404(id)

    db.session.delete(fornecedor)
    db.session.commit()

    flash('Fornecedor deletado com sucesso')

    return redirect(url_for('admin.list_fornecedores'))

    return render_template(title="Deletar fornecedor")


"""
Rotas para cadastro de categorias
"""
@admin.route('/categorias', methods=['GET', 'POST'])
@login_required
def list_categorias():
    check_admin()

    categorias = Categoria.query.all()

    return render_template('admin/categorias/list.html', categorias=categorias, title="Lista de Categorias Cadastradas")


@admin.route('/categorias/add', methods=['GET', 'POST'])
@login_required
def add_categoria():
    check_admin()

    form = CategoriaForm()

    if form.validate_on_submit():
        categoria = Categoria(nome=form.nome.data,
                              descricao=form.descricao.data)
        try:
            db.session.add(categoria)
            db.session.commit()

            flash('Categoria adicionada com sucesso!')
        except:
            flash('Erro ao adicionar categoria!')

        return redirect(url_for('admin.list_categorias'))

    return render_template('admin/categorias/add.html',
                           form=form,
                           title="Adicionar Categoria")


@admin.route('/categorias/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_categoria(id):
    check_admin()

    categoria = Categoria.query.get_or_404(id)

    form = CategoriaEditForm(obj=categoria)

    if form.validate_on_submit():
        categoria.nome = form.nome.data
        categoria.descricao = form.descricao.data

        db.session.commit()

        flash('Categoria editada com sucesso!')

        return redirect(url_for('admin.list_categorias'))

    return render_template('admin/categorias/edit.html',
                           form=form,
                           categoria=categoria,
                           title="Editar categoria")


@admin.route('/categorias/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_categoria(id):
    check_admin()

    categoria = Categoria.query.get_or_404(id)
    produtos_relacionados = Produto.query.filter_by(id_categoria=id).all()

    if len(produtos_relacionados) > 0:
        flash('Não é possível deletar a categoria: Existem produtos ativos pertencentes a esta categoria')
    else:
        db.session.delete(categoria)
        db.session.commit()

        flash('Categoria deletada com sucesso')

    return redirect(url_for('admin.list_categorias'))

    return render_template(title="Deletar categoria")


"""
Rotas para cadastro de produtos
"""
@admin.route('/produtos', methods=['GET', 'POST'])
@login_required
def list_produtos():
    check_admin()

    produtos = Produto.query.all()

    return render_template('admin/produtos/list.html', produtos=produtos, title="Lista de Produtos Cadastrados")


@admin.route('/produtos/add', methods=['GET', 'POST'])
@login_required
def add_produto():
    check_admin()

    fornecedores = Fornecedor.query.all()
    categorias = Categoria.query.all()

    if fornecedores is None or len(fornecedores) == 0:
        flash('Não existem fornecedores cadastrados!')

        return redirect(url_for('admin.list_produtos'))
    elif categorias is None or len(categorias) == 0:
        flash('Não existem categorias cadastradas!')

        return redirect(url_for('admin.list_produtos'))
    else:
        form = ProdutoForm()
        form.fornecedor.choices = [(f.id, f.nome_fantasia) for f in fornecedores]
        form.categoria.choices = [(c.id, c.nome) for c in categorias]

        if form.validate_on_submit():
            produto = Produto(nome=form.nome.data,
                              descricao=form.descricao.data,
                              preco=form.preco.data,
                              quantidade=form.quantidade.data,
                              #img=form.imagem.data,
                              id_categoria=form.categoria.data,
                              id_fornecedor=form.fornecedor.data)
            try:
                db.session.add(produto)
                db.session.commit()

                flash('Produto adicionado com sucesso!')
            except Exception as e:
                print(str(e))
                flash('Erro ao adicionar produto!')

            return redirect(url_for('admin.list_produtos'))

        return render_template('admin/produtos/add.html',
                               form=form,
                               title="Adicionar Produto")


@admin.route('/produtos/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_produto(id):
    check_admin()

    produto = Produto.query.get_or_404(id)

    fornecedores = Fornecedor.query.all()
    categorias = Categoria.query.all()

    if fornecedores is None or len(fornecedores) == 0:
        flash('Não existem fornecedores cadastrados!')

        return redirect(url_for('admin.list_produtos'))
    elif categorias is None or len(categorias) == 0:
        flash('Não existem categorias cadastradas!')

        return redirect(url_for('admin.list_produtos'))

    form = ProdutoEditForm(obj=produto)
    form.fornecedor.choices = [(f.id, f.nome_fantasia) for f in fornecedores]
    form.categoria.choices = [(c.id, c.nome) for c in categorias]

    if form.validate_on_submit():
        produto.nome = form.nome.data
        produto.descricao = form.descricao.data
        produto.preco = form.preco.data
        produto.quantidade = form.quantidade.data
        #produto.img = form.imagem.data
        produto.id_categoria = form.categoria.data
        produto.id_fornecedor = form.fornecedor.data

        db.session.commit()
        flash('Produto editado com sucesso!')

        return redirect(url_for('admin.list_produtos'))

    return render_template('admin/produtos/edit.html',
                           form=form,
                           produto=produto,
                           title="Editar produto")


@admin.route('/produtos/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_produto(id):
    check_admin()

    produto = Produto.query.get_or_404(id)

    db.session.delete(produto)
    db.session.commit()

    flash('Produto deletado com sucesso')

    return redirect(url_for('admin.list_produtos'))

    return render_template(title="Deletar produto")
