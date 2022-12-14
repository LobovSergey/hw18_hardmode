from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    users = db.relationship('Movie')


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()
