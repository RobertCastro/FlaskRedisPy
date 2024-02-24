from flask import Flask
from flask_restful import Api

from vistas.vista_search_resource import SearchResource

app = Flask(__name__)
api = Api(app)


app.run(port=6000)

api.add_resource(SearchResource, '/api/v1/search')


if __name__ == '__main__':
    app.run(debug=True)