from ping_service_log import registrar_ping_recibido
from failures_ping_service_log import registrar_ping_falla
from flask_restful import Resource
from flask import request  # Asegúrate de importar request
import uuid
import datetime

class PingResource(Resource):
    def get(self):
        new_ping_id = str(uuid.uuid4())
        new_ping_datetime = str(datetime.datetime.now())
        try:
            simulate_failure = request.args.get('simulate_failure', type=bool, default=False)
            failure_uuid = request.args.get('failure_uuid', default=new_ping_id)

            if simulate_failure:
                # Si se solicita simular un fallo, se utiliza el UUID proporcionado o se genera uno nuevo
                raise Exception(f"{failure_uuid};{new_ping_datetime}")

            # Si no se solicita simular un fallo, se registra el ping como antes
            registrar_ping_recibido.delay(ping_id=new_ping_id, ping_datetime=new_ping_datetime)
            return {
                'status': 'success',
                'message': 'Echo',
                "ping_id": new_ping_id,
                "ping_datetime": new_ping_datetime
            }, 200

        except Exception as e:
            error_message = str(e)
            # En caso de fallo, se registra el fallo con el UUID proporcionado o el generado
            registrar_ping_falla.delay(error_message)
            return {
                'status': 'success',
                "ping_id": failure_uuid,  # Usa el UUID proporcionado o el generado
                "ping_datetime": new_ping_datetime,
                'message': 'Ping failure received.'
            }, 200
