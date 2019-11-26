import logging

from flask_restful import Resource, reqparse
from marshmallow_sqlalchemy import ModelSchema

from dropshipping import db
from dropshipping.models.fornecedor import Fornecedor


class FornecedorSchema(ModelSchema):
    class Meta:
        model = Fornecedor


class ListaFornecedorAPI(Resource):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome_fantasia', type=str, required=True,
                                 help='É necessário informar o nome do fornecedor',
                                 location='json')
        self.parser.add_argument('cnpj', type=str, required=True,
                                 help='É necessário informar o CNPJ do fornecedor',
                                 location='json')
        self.parser.add_argument('url', type=str, required=True,
                                 help='É necessário informar a URL de integração',
                                 location='json')
        self.parser.add_argument('ativo', type=bool, location='json')

        super(ListaFornecedorAPI, self).__init__()

    def get(self):
        schema = FornecedorSchema()
        fornecedores = Fornecedor.query.all()
        result = list()

        for fornecedor in fornecedores:
            fornecedor_as_dict = schema.dump(fornecedor)
            result.append(fornecedor_as_dict)

        return {'message': 'operação realizada com sucesso', 'fornecedores': result}, 200

    def post(self):
        args = self.parser.parse_args()
        fornecedor = Fornecedor(nome_fantasia=args['nome_fantasia'],
                                cnpj=args['cnpj'],
                                url=args['url'])

        try:
            self.logger.info('Persistindo fornecedor no banco de dados')

            db.session.add(fornecedor)
            db.session.commit()

            return {'message': 'operação realizada com sucesso'}, 200
        except Exception as e:
            return {'message': 'erro ao executar a operação', 'error': str(e)}, 400


class FornecedorAPI(Resource):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nome_fantasia', type=str, required=True,
                                 help='É necessário informar o nome do fornecedor',
                                 location='json')
        self.parser.add_argument('cnpj', type=str, required=True,
                                 help='É necessário informar o CNPJ do fornecedor',
                                 location='json')
        self.parser.add_argument('url', type=str, required=True,
                                 help='É necessário informar a URL de integração',
                                 location='json')
        self.reqparse.add_argument('ativo', type=bool, location='json')

        super(FornecedorAPI, self).__init__()

    def get(self, id):
        fornecedor = Fornecedor.query.get_or_404(id, description='fornecedor não encontrado')

        fornecedor_as_dict = FornecedorSchema().dump(fornecedor)

        return {'message': 'operação realizada com sucesso', 'fornecedor': fornecedor_as_dict}, 200

    def put(self, id):
        fornecedor = Fornecedor.query.get_or_404(id, description='fornecedor não encontrado')

        args = self.parser.parse_args()

        fornecedor.nome = args['nome']
        fornecedor.descricao = args['descricao']

        try:
            self.logger.info('Persistindo fornecedor no banco de dados')

            db.session.commit()

            return {'message': 'operação realizada com sucesso'}, 200
        except Exception as e:
            return {'message': 'erro ao executar a operação', 'error': str(e)}, 400

    def delete(self, id):
        pass
