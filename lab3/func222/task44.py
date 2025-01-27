#Write a function that takes a list of movies and computes the average IMDB score
from movies_data import movies
def average_imdb_score(movies):
    if not movies: 
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

average_score = average_imdb_score(movies)
print(f'Average IMDB score: {average_score}')
