from dao.model.movie_model import Movie


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movie_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_movie_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def create_movie(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def edit_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete_movie(self, uid):
        self.session.query(Movie).filter(Movie.id == uid).delete()
        self.session.commit()
