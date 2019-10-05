from flask import Flask, request
from flask_restful import reqparse, Resource, Api
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('left', type=float)
parser.add_argument('right', type=float)


class EndpointSuma(Resource):
    def get(self):
        return {'Hola': 'Mundo'}

    def post(self):
        args = parser.parse_args()
        return {'result':args['left'] + args['right']}

class HealthCheck(Resource):
    def get(self):
        return "I'm alive!"

api.add_resource(EndpointSuma, '/compute-binary')
api.add_resource(HealthCheck, '/utils/health')

if __name__ == '__main__':
    app.run(debug=True)