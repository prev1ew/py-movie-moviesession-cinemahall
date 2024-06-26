from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    result = Movie.objects.all()
    if genres_ids:
        result = result.filter(genres__id__in=genres_ids)
    if actors_ids:
        result = result.filter(actors__id__in=actors_ids)
    return result


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    created_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        created_movie.genres.set(genres_ids)

    if actors_ids:
        created_movie.actors.set(actors_ids)

    return created_movie
