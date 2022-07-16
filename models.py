from config import db
from marshmallow import Schema, fields


# Models
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# Schemas
class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Pluck(GenreSchema, 'name')
    director = fields.Pluck(DirectorSchema, 'name')


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
