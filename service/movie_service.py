class MovieService:

    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create_movie(self, data):
        return self.dao.create_movie(data)

    def edit_movie(self, mid, data):
        edited_movie = self.get_one(mid)
        edited_movie.title = data.get('title')
        edited_movie.description = data.get('description')
        edited_movie.trailer = data.get('trailer')
        edited_movie.year = data.get('year')
        edited_movie.rating = data.get('rating')
        edited_movie.genre_id = data.get('genre_id')
        edited_movie.director_id = data.get('director_id')
        self.dao.edit_movie(edited_movie)

    def delete_movie(self, uid):
        return self.dao.delete_movie(uid)

    def search_movie(self, data):
        directors_id = data.get('directors_id')
        genre_id = data.get('genre_id')
        year = data.get('year')
        result = None
        if directors_id:
            result = self.dao.get_movie_by_director(directors_id)
        if genre_id:
            result = self.dao.get_movie_by_genre(genre_id)
        if year:
            result = self.dao.get_movie_by_year(year)
        return result
