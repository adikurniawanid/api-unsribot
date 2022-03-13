from flask import Flask
from flask_restful import reqparse, Api, Resource
from Controller.Preprocessing import Preprocessing
from Controller.Parser import Parser
from Controller.Translator import Translator
from Model.Connection import querySQL


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('nlParam')


class NaturalLanguage(Resource):
    def get(self):
        return {'message': 'api-unsribot'}

    def post(self):
        __preprocessing = Preprocessing()
        __kalimatPerintah = parser.parse_args()
        __token = __preprocessing.run(__kalimatPerintah['nlParam'])
        __parser = Parser(__token)
        __translator = Translator(__token)
        __query = __translator.run()
        __queryResult = querySQL(__query)

        result = {
            'kalimat': __token,
            'isPerintah': __parser.getPerintahTeridentifikasi(),
            'identifikasiTabel': __parser.getTabelTeridentifikasi(),
            'identifikasiKolomByTabel': __parser.getKolomTeridentifikasiByTabel(),
            'identifikasiKondisi': __parser.getKondisiTeridentifikasi(),
            'identifikasiKolomKondisi': __parser.getKolomKondisiTeridentifikasi(),
            'identifikasiAtributKondisi': __parser.getAtributKondisiTeridentifikasi(),
            'identifikasiOperator': __parser.getOperatorLogikaTeridentifikasi(),
            'query': __query,
            'queryResult': __queryResult
        }
        return result, 201


api.add_resource(NaturalLanguage, '/')

if __name__ == '__main__':
    app.run(debug=True)
