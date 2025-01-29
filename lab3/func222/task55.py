#Write a function that takes a category and computes the average IMDB score.

from movies_data import movies

def averagee(movies, category_name):
    filtered_movies = [movie for movie in movies if movie["category"].lower() == category_name.lower()]
    if not filtered_movies:
        return 0
    # Calculate the total score of the filtered movies
    total_score = sum(movie["imdb"] for movie in filtered_movies)
    return total_score / len(filtered_movies)
romance_average_score = averagee(movies, "Romance")
print(f'Average IMDB score for Romance category: {romance_average_score}')
