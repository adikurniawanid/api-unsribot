from flask import Flask
from flask_restful import reqparse, Api, Resource
from Preprocessing import pre
from Processing import identifikasiKolomByTabel, identifikasiKondisi, identifikasiOperatorLogika, isPerintah, identifikasiTabel, identifikasiKolom
from QueryForming import queryForming

app = Flask(__name__)
api = Api(app)

kalimatPerintah = ''

parser = reqparse.RequestParser()
parser.add_argument('NL')


class NaturalLanguage(Resource):
    def post(self):
        kalimatPerintah = parser.parse_args()
        kalimatPerintah = pre(kalimatPerintah['NL'])
        result = {
            # 'kalimat': kalimatPerintah,
            'isPerintah': isPerintah(kalimatPerintah),
            'identifikasiTabel': identifikasiTabel(kalimatPerintah),
            'identifikasiKolomByTabel': identifikasiKolomByTabel(kalimatPerintah),
            #   'identifikasiKondisi': identifikasiKondisi(kalimatPerintah),
            #   'identifikasiOperator': identifikasiOperatorLogika(kalimatPerintah),
            'query': queryForming(kalimatPerintah)
        }
        # query = {'query': queryForming(kalimatPerintah)}

        return result, 201


api.add_resource(NaturalLanguage, '/nl')

if __name__ == '__main__':
    app.run(debug=True)
