from flask import Flask
from flask_restful import reqparse, Api, Resource
from Controller.Preprocessing import pre
from Controller.Processing import identifikasiKolomByTabel, identifikasiKolomKondisi, isPerintah, identifikasiTabel, identifikasiKondisi, identifikasiOperatorLogika
from Controller.QueryForming import queryForming

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('nlParam')


class NaturalLanguage(Resource):
    def get(self):
        return {'message': 'api-unsribot'}

    def post(self):
        kalimatPerintah = parser.parse_args()
        kalimatPerintah = pre(kalimatPerintah['nlParam'])
        result = {
            'kalimat': kalimatPerintah,
            'isPerintah': isPerintah(kalimatPerintah),
            'identifikasiTabel': identifikasiTabel(kalimatPerintah),
            'identifikasiKolomByTabel': identifikasiKolomByTabel(kalimatPerintah),
            'identifikasiKondisi': identifikasiKondisi(kalimatPerintah),
            'identifikasiOperator': identifikasiOperatorLogika(kalimatPerintah),
            'identifikasiKolomKondisi': identifikasiKolomKondisi(kalimatPerintah),
            'query': queryForming(kalimatPerintah)
        }
        return result, 201


api.add_resource(NaturalLanguage, '/')

if __name__ == '__main__':
    app.run(debug=True)
