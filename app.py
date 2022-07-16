from config import *
from flask import Flask, request
from flask_restx import Resource
from models import *


@movies_ns.route('/')
class MoviesView(Resource):
    """Получаем данные о фильме с именем режиссера, названием жанра
    и фильтром по id режиссера, id жанра"""

    def get(self):

        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)

        if director_id and genre_id:
            movies = db.session.query(Movie) \
                .join(Movie.genre).join(Movie.director) \
                .filter(Movie.director_id == director_id, Movie.genre_id == genre_id) \
                .all()

            if not movies:
                return f"no movie with 'director_id' - {director_id}" \
                       f" and 'genre_id' - {genre_id}", 204
            else:
                return movies_schema.dump(movies), 200

        if director_id:
            movies = db.session.query(Movie) \
                .join(Movie.genre).join(Movie.director) \
                .filter(Movie.director_id == director_id) \
                .all()

            if not movies:
                return f"no movie with 'director_id' - {director_id}", 204
            else:
                return movies_schema.dump(movies), 200

        if genre_id:
            movies = db.session.query(Movie) \
                .join(Movie.genre).join(Movie.director) \
                .filter(Movie.genre_id == genre_id) \
                .all()

            if not movies:
                return f"no movie with 'genre_id' - {genre_id}", 204
            else:
                return movies_schema.dump(movies), 200

        else:
            all_movies = db.session.query(Movie) \
                .join(Movie.genre).join(Movie.director) \
                .all()

            return movies_schema.dump(all_movies), 200


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    """Получаем данные о фильме по id"""

    def get(self, movie_id):
        movie = db.session.query(Movie).get(movie_id)
        if movie is not None:
            return movie_schema.dump(movie), 200
        return f"no movie with 'id' - {movie_id}", 404


if __name__ == '__main__':
    app.run(debug=True)
