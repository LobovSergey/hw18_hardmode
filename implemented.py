from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService
from setup_db import db
from dao.movie_dao import MoviesDAO

movie_dao = MoviesDAO(db.session)
movie_service = MovieService(movie_dao)
director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
