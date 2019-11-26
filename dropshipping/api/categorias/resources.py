import logging

from flask_restful import Resource, reqparse
from marshmallow_sqlalchemy import ModelSchema

from dropshipping import db
from dropshipping.models.categoria import Categoria


class CategoriaSchema(ModelSchema):
    class Meta:
        model = Categoria


class ListaCategoriaAPI(Resource):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', type=str, required=True,
                                 help='É necessário informar o nome da categoria',
                                 location='json')
        self.parser.add_argument('descricao', type=str, required=True,
                                 help='É necessário informar a descrição da categoria',
                                 location='json')

        super(ListaCategoriaAPI, self).__init__()

    def get(self):
        schema = CategoriaSchema()
        categorias = Categoria.query.all()
        result = list()

        for categoria in categorias:
            categoria_as_dict = schema.dump(categoria)
            result.append(categoria_as_dict)

        return {'message': 'operação realizada com sucesso', 'categorias': result}, 200

    def post(self):
        args = self.parser.parse_args()
        nova_categoria = Categoria(nome=args['nome'], descricao=args['descricao'])

        try:
            self.logger.info('Persistindo no banco de dados')

            db.session.add(nova_categoria)
            db.session.commit()

            return {'message': 'operação realizada com sucesso'}, 200
        except Exception as e:
            return {'message': 'erro ao executar a operação', 'error': str(e)}, 400


class CategoriaAPI(Resource):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome', type=str, required=True,
                                 help='É necessário informar o nome da categoria',
                                 location='json')
        self.parser.add_argument('descricao', type=str, required=True,
                                 help='É necessário informar a descrição da categoria',
                                 location='json')

        super(CategoriaAPI, self).__init__()

    def get(self, id):
        categoria = Categoria.query.get_or_404(id, description='categoria não encontrada')

        categoria_as_dict = CategoriaSchema().dump(categoria)

        return {'message': 'operação realizada com sucesso', 'categoria': categoria_as_dict}, 200

    def put(self, id):
        categoria = Categoria.query.get_or_404(id, description='categoria não encontrada')

        args = self.parser.parse_args()

        categoria.nome = args['nome']
        categoria.descricao = args['descricao']

        try:
            self.logger.info('Persistindo no banco de dados')

            db.session.commit()

            return {'message': 'operação realizada com sucesso'}, 200
        except Exception as e:
            return {'message': 'erro ao executar a operação', 'error': str(e)}, 400

    def delete(self, id):
        pass
