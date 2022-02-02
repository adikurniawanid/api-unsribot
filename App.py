from flask import Flask
from flask_restful import reqparse, Api, Resource
from Controller.Preprocessing import Preprocessing
from Controller.Processing import Processing
from Controller.QueryForming import QueryForming

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('nlParam')


class NaturalLanguage(Resource):
    def get(self):
        return {'message': 'api-unsribot'}

    def post(self):
        preprocessing = Preprocessing()
        processing = Processing()
        kalimatPerintah = parser.parse_args()
        kalimatPerintah = preprocessing.pre(kalimatPerintah['nlParam'])
        queryForming = QueryForming(kalimatPerintah)

        result = {
            'kalimat': kalimatPerintah,
            'isPerintah': processing.isPerintah(kalimatPerintah),
            'identifikasiTabel': processing.identifikasiTabel(kalimatPerintah),
            'identifikasiKolomByTabel': processing.identifikasiKolomByTabel(kalimatPerintah),
            'identifikasiKondisi': processing.identifikasiKondisi(kalimatPerintah),
            'identifikasiOperator': processing.identifikasiOperatorLogika(kalimatPerintah),
            'identifikasiKolomKondisi': processing.identifikasiKolomKondisi(kalimatPerintah),
            'query': queryForming.queryForming()
        }
        return result, 201


api.add_resource(NaturalLanguage, '/')

if __name__ == '__main__':
    app.run(debug=True)
