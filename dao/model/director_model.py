from marshmallow import Schema, fields

from setup_db import db


class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    users = db.relationship('Movie')


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()