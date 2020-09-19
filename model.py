import jwt, bcrypt, configparser
from flask import request, jsonify
from flask_restx import Resource, Api, Namespace, fields


config = configparser.ConfigParser()
config.read('config.ini')

jwt_secret_key = config['DEFAULT']['JWT_SECRET']
algorithm = "HS256"

users = {}

Federated = Namespace(
    name="Auth",
    description="Global Model",
)

user_fields = Federated.model('User', {  # Model 객체 생성
    'name': fields.String(description='a User Name', required=True, example="justkode")
})

user_fields_auth = Federated.inherit('User Auth', user_fields, {
    'password': fields.String(description='Password', required=True, example="password")
})

jwt_fields = Federated.model('JWT', {
    'Authorization': fields.String(description='Authorization which you must inclued in header', required=True, example="eyJ0e~~~~~~~~~")
})


@Federated.route('/weight/update')
class GlobalModel(Resource):
    @Federated.doc(responses={200: 'Success'})
    @Federated.doc(responses={404: 'Authentication failed'})
    def post(self):
        header = request.headers.get('authorization')  # 헤더에 authorization 부분을 가져옴.
        if header == None:
            return jsonify({"message": "Invalid Header Type"}), 404
        data = jwt.decode(header, jwt_secret_key, algorithm=algorithm)


        return jsonify({data}), 200
