#Write a function that takes a category and computes the average IMDB score.
from movies_data import movies

def average_imdb_score_by_category(movies, category_name):
    filtered_movies = [movie for movie in movies if movie["category"].lower() == category_name.lower()]
    
    # If no movies are found in the given category
    if not filtered_movies:
        return 0
    
    # Calculate the total score of the filtered movies
    total_score = sum(movie["imdb"] for movie in filtered_movies)
    
    # Return the average IMDB score
    return total_score / len(filtered_movies)

romance_average_score = average_imdb_score_by_category(movies, "Romance")
print(f'Average IMDB score for Romance category: {romance_average_score}')
