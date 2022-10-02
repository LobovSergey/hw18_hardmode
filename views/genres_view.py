from flask_restx import Namespace, Resource

from dao.model.genre_model import genre_schema, genres_schema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenreView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        return genre_schema.dump(genre_service.get_one(uid)), 200
