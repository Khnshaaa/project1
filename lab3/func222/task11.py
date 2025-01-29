#Write a function that takes a single movie and returns True if its IMDB score is above 5.5

from movies_data import movies

def is_highly_rated(movie):
    return movie["imdb"] > 5.5
for movie in movies:
    print(f'{movie["name"]}: {is_highly_rated(movie)}')
