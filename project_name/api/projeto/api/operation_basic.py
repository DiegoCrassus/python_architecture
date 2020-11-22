import logging

import settings
from flask import request
from flask_restplus import Resource
from projeto.restplus import api
from projeto.constants import CodeHttp, Message
from projeto.utils import doc_swagger
from projeto.restplus import objLogger, objResponse

log = logging.getLogger(__name__)
ns = api.namespace(settings.ENDPOINTS, description='Post operação.')


@ns.route(settings.ROUTE)
class PostsCollection(Resource):

    def get(self):
        """
        Método de teste GET
        Arguments: sexo - hdjhsdhjds, idade - jdjdjdjdjdjd
        """
        objLogger.warning(Message.WARNING_TESTE)

    @api.response(200, 'Enviado com sucesso.')
    @api.marshal_with(doc_swagger.OUTPUT_DATA)
    def post(self):
        """
        Método de teste POST
        """
        objLogger.debug(Message.REQUEST)
        request_data = request.get_json()

        try:
            teste = request_data["file"]

        except KeyError as error:
            response = objResponse.send_exception(objError=error, messages=Message.ERROR_NO_KEY_REQUEST, status=CodeHttp.ERROR_500)
            objLogger.error(messages=Message.ERROR_NO_KEY_REQUEST)

        except TypeError as error:
            response = objResponse.send_exception(objError=error, messages=Message.ERROR_NO_REQUEST_DATA, status=CodeHttp.ERROR_500)
            objLogger.error(messages=Message.ERROR_NO_REQUEST_DATA)

        else:
            response = objResponse.send_success(messages=Message.SUCESS_EXEMPLO, status=CodeHttp.SUCCESS_200, data=teste)
            objLogger.success(messages=Message.SUCESS_EXEMPLO)

        return response
