from flask_restful import Api, Resource, reqparse
from failures_search_user_log import registrar_falla_en_busqueda

import datetime

class SearchResource(Resource):

    def get(self):
        
        return {'status':'success', 'message': 'Email encontrado'}, 200