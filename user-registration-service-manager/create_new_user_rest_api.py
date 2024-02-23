from flask import Flask
from flask_restful import Api, Resource, reqparse
from user_registration_service_principal import registrar_usuario_principal
from ping_service_log import registrar_ping_recibido
from failures_with_user_registration_log import registrar_falla_en_registro

import uuid
import datetime


app = Flask(__name__)
api = Api(app)


class UserResource(Resource):

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, required=True, help='Email address is required')
            parser.add_argument('simulate_failure', type=bool, required=False)
            parser.add_argument('failure_uuid', type=str, required=False)
            args = parser.parse_args()
            email = args['email']
            
            if 'simulate_failure' in args and args['simulate_failure']==True:
                failure_uuid = args['failure_uuid']
                failure_datetime = str(datetime.datetime.now())
                raise Exception(str(failure_uuid) + ";" + email + ";" + str(failure_datetime))

            registrar_usuario_principal.delay(email)

        except Exception as e:
            error_message = str(e)
            registrar_falla_en_registro.delay(error_message)
            return {
                'status':'success', 
                'message': 'Email received successfully. We are experiencing latencies but we received your email and we will register you.'
            }, 200

        return {'status':'success', 'message': 'Email received successfully'}, 200
    

class PingResource(Resource):
    def get(self):
        new_ping_id = str(uuid.uuid4())
        new_ping_datetime = str(datetime.datetime.now())
        registrar_ping_recibido.delay(ping_id=new_ping_id, ping_datetime=new_ping_datetime)
        return {
            'status': 'success', 
            'message': 'Echo', 
            "ping_id":new_ping_id, 
            "ping_datetime":new_ping_datetime
        }, 200

    
api.add_resource(UserResource, '/api/v1/users')
api.add_resource(PingResource, '/ping')

if __name__ == '__main__':
    app.run(debug=False)