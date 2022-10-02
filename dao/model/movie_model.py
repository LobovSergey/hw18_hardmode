from marshmallow import Schema, fields

from setup_db import db


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.String(100))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    # genres = db.relationship('Genre')
    # directors = db.relationship('Director')


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Str()
    genre_id = fields.Int()
    director_id = fields.Int()


movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()
