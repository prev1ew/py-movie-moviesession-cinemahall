import init_django_orm
from services.cinema_hall import create_cinema_hall, get_cinema_halls

from services.movie import get_movies, get_movie_by_id, create_movie
from services.movie_session import create_movie_session, get_movies_sessions, update_movie_session, \
    delete_movie_session_by_id

# create_movie_session("2024-01-01", 1, 1)
# print(get_movies_sessions("2024-01-01"))
print(get_movies_sessions())
el = update_movie_session(2, "2024-01-01", 1, 1)
print(el)
