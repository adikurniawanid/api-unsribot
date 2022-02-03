from flask import Flask
from flask_restful import reqparse, Api, Resource
from Controller.Preprocessing import Preprocessing
from Controller.Parser import Parser
from Controller.QueryForming import QueryForming

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
        __queryForming = QueryForming(__token)

        result = {
            'kalimat': __token,
            'isPerintah': __parser.getPerintahTeridentifikasi(),
            'identifikasiTabel': __parser.getTabelTeridentifikasi(),
            'identifikasiKolomByTabel': __parser.getKolomTeridentifikasiByTabel(),
            'identifikasiKondisi': __parser.getKondisiTeridentifikasi(),
            'identifikasiKolomKondisi': __parser.getKolomKondisiTeridentifikasi(),
            'identifikasiAtributKondisi': __parser.getAtributKondisiTeridentifikasi(),
            'identifikasiOperator': __parser.getOperatorLogikaTeridentifikasi(),
            'query': __queryForming.run()
        }
        return result, 201


api.add_resource(NaturalLanguage, '/')

if __name__ == '__main__':
    app.run(debug=True)
