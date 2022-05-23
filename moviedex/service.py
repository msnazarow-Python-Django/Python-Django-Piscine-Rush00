from __future__ import annotations
import random
import requests
from django.conf import settings


class Moviemon:
    def __init__(self, movie: dict):
        self.id: str = movie['imdbID']
        self.title: str = movie['Title']
        self.director: str = movie['Director']
        self.year: str = movie['Year']
        self.rating: str = movie['imdbRating']
        self.poster_url: str = movie['Poster']
        self.synopsis: str = movie['Plot']
        self.actors: str = movie['Actors']

    @staticmethod
    def get_movies() -> dict[str, Moviemon]:
        """

        @return: Returns a dictionary with a length of 10 consist of key: 'movie_id', value: 'Moviemon'
        """
        movies = {}
        ids = tuple(settings.MOVIE_IDS)
        while len(movies) < 10:
            random_id = random.choice(ids)
            if random_id not in movies:
                movie = Moviemon.__get_movie_by_id(random_id)
                if movie:
                    movies.update({random_id: Moviemon(movie)})
        return movies

    @staticmethod
    def __get_movie_by_id(movie_id: str) -> dict | None:
        params = {
            'apikey': settings.OMDB_APIKEY,
            'i': movie_id
        }
        response = requests.get(
            url=settings.OMDB_URL,
            params=params
        )
        try:
            response.raise_for_status()
        except requests.RequestException:
            return None
        movie_info = response.json()
        return movie_info if 'Error' not in movie_info else None
