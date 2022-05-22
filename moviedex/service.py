import random
import requests
from django.conf import settings


def get_random_movie_or_none():
    random_movie_id = random.randint(1, 9999999)
    params = {
        'apikey': settings.OMDB_APIKEY,
        'i': f'tt{random_movie_id:0>7}'
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

def get_10_movies():
    movies = []
    while len(movies) < 10:
        movie = get_random_movie_or_none()
        if movie:
            movies.append(movie)
    return movies
