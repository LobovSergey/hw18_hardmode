from flask import request
from flask_restx import Namespace, Resource

from dao.model.movie_model import movies_schema, movie_schema
from implemented import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        data = request.args
        if data:
            return movies_schema.dump(movie_service.search_movie(data)), 200
        return movies_schema.dump(movie_service.get_all()), 200

    def post(self):
        data = request.json
        movie_service.create_movie(data)
        return 'created', 201


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        return movie_schema.dump(movie_service.get_one(uid)), 200

    def delete(self, uid):
        movie_service.delete_movie(uid)
        return 'deleted', 204

    def put(self, uid):
        data = request.json
        movie_service.edit_movie(uid, data)
        return 'edited', 204
