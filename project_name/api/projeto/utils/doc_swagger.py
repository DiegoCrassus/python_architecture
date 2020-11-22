from flask_restplus import fields
from projeto.restplus import api

# expected input values of api
INPUT_DATA = api.model('input',
                       {'file': fields.String(required=True,
                                              description="image in base64",
                                              example="iVBORw0KGgoAAAANSUhEUgAAE...")})

OUTPUT_DATA = api.model('Output',
                        {'message': fields.Raw(required=True,
                                                   description='[Sucess or Error mensage]'),
                         'status': fields.String(required=True,
                                                 description='Status code'),
                         'data': fields.Raw(required=False,
                                            description="list of image or text in base64")})
