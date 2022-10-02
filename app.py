from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.director_model import Director
from dao.model.genre_model import Genre
from dao.model.movie_model import Movie
from setup_db import db
from views.directors_view import directors_ns
from views.genres_view import genres_ns
from views.movies_view import movies_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        m1 = Movie(id=1, title='Title 1', description='description 1', trailer='trailer 1', year=8212, rating='R1',
                   genre_id=1, director_id=3)
        m2 = Movie(id=2, title='Title 2', description='description 2', trailer='trailer 2', year=15789, rating='R2',
                   genre_id=2, director_id=5)
        m3 = Movie(id=3, title='Title 3', description='description 3', trailer='trailer 3', year=55, rating='R1',
                   genre_id=3, director_id=6)
        m4 = Movie(id=4, title='Title 4', description='description 4', trailer='trailer 4', year=1496, rating='R2',
                   genre_id=4, director_id=2)
        m5 = Movie(id=5, title='Title 5', description='description 5', trailer='trailer 5', year=778, rating='R3',
                   genre_id=4, director_id=5)
        m6 = Movie(id=6, title='Title 6', description='description 6', trailer='trailer 6', year=12, rating='R3',
                   genre_id=2, director_id=1)
        m7 = Movie(id=7, title='Title 7', description='description 7', trailer='trailer 7', year=266, rating='R2',
                   genre_id=1, director_id=2)
        m8 = Movie(id=8, title='Title 8', description='description 8', trailer='trailer 8', year=12, rating='R3',
                   genre_id=3, director_id=1)
        m9 = Movie(id=9, title='Title 9', description='description 9', trailer='trailer 9', year=15789, rating='R1',
                   genre_id=1, director_id=3)

        d1 = Director(id=1, name='Gary Oldman')
        d2 = Director(id=2, name='Ben Stiller')
        d3 = Director(id=3, name='Jora Kryjovnikov')
        d4 = Director(id=4, name='Evhenii Bajenov')
        d5 = Director(id=5, name='Sergey Lobov')
        d6 = Director(id=6, name='Mike Tyson')

        g1 = Genre(id=1, name='Horror')
        g2 = Genre(id=2, name='Comedy')
        g3 = Genre(id=3, name='Travel')
        g4 = Genre(id=4, name='Show')
        g5 = Genre(id=5, name='Music')

        with db.session.begin():
            db.session.add_all([m1, m2, m3, m4, m5, m6, m7, m8, m9])
            db.session.add_all([d1, d2, d3, d4, d5, d6])
            db.session.add_all([g1, g2, g3, g4, g5])


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="localhost", port=10001)
