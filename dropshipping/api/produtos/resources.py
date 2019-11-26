from flask_restful import Resource
from marshmallow_sqlalchemy import ModelSchema

from dropshipping.models.produto import Produto
from dropshipping.models.fornecedor import Fornecedor
from dropshipping.models.categoria import Categoria


class ProdutoSchema(ModelSchema):
    class Meta:
        model = Produto


class CategoriaSchema(ModelSchema):
    class Meta:
        model = Categoria


class FornecedorSchema(ModelSchema):
    class Meta:
        model = Fornecedor


class ListaProdutoAPI(Resource):
    def __init__(self):
        super(ListaProdutoAPI, self).__init__()

    def get(self):
        schema = ProdutoSchema()
        produtos = Produto.query.all()
        result = list()

        try:
            for p in produtos:
                produto = schema.dump(p)

                c = Categoria.query.get(produto['categoria'])
                f = Fornecedor.query.get(produto['fornecedor'])

                produto['categoria'] = CategoriaSchema().dump(c)['nome']
                produto['fornecedor'] = FornecedorSchema().dump(f)['nome_fantasia']

                result.append(produto)
        except Exception as e:
            return {'message': 'erro ao executar a operação', 'error': str(e)}, 400

        return {'message': 'operação realizada com sucesso', 'produtos': result}, 200

    def post(self):
        pass


class ProdutoAPI(Resource):
    def __init__(self):
        super(ProdutoAPI, self).__init__()

    def get(self, id):
        p = Produto.query.get_or_404(id, description='produto não encontrado')

        try:
            produto = ProdutoSchema().dump(p)

            c = Categoria.query.get(produto['categoria'])
            f = Fornecedor.query.get(produto['fornecedor'])

            produto['categoria'] = CategoriaSchema().dump(c)['nome']
            produto['fornecedor'] = FornecedorSchema().dump(f)['nome_fantasia']

        except Exception as e:
            return {'message': 'erro ao executar a operação', 'error': str(e)}, 400

        return {'message': 'operação realizada com sucesso', 'produto': produto}, 200

    def put(self, id):
        pass

    def delete(self, id):
        pass
