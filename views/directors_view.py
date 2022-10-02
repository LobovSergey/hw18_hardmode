from flask_restx import Namespace, Resource

from dao.model.director_model import director_schema, directors_schema
from implemented import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return directors_schema.dumps(director_service.get_all()), 200


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        return director_schema.dumps(director_service.get_one(uid)), 200
