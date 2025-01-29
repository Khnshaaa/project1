#Write a function that returns a sublist of movies with an IMDB score above 5.5.
from movies_data import movies

def get_highly_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
highly_rated_movies = get_highly_rated_movies(movies)

for movie in highly_rated_movies:
    print(f'{movie["name"]}: {movie["imdb"]}')
