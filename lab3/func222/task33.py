#Write a function that takes a category name and returns just those movies under that category.
from movies_data import movies

def get_movies_by_category(movies, category_name):
    return [movie for movie in movies if movie["category"].lower() == category_name.lower()]

romance_movies = get_movies_by_category(movies, "Romance")
for movie in romance_movies:
    print(f'{movie["name"]}: {movie["imdb"]} - {movie["category"]}')
