movies_count = int(input())

min_rating = 11
max_rating = 0

max_rating_movie_name = ''
min_rating_movie_name = ''

total_rating_sum=0

for movie in range(movies_count):
    movie_name = input()
    movie_rating = float(input())
    total_rating_sum+=movie_rating

    if movie_rating > max_rating:
        max_rating = movie_rating
        max_rating_movie_name = movie_name

    if movie_rating<min_rating:
        min_rating=movie_rating
        min_rating_movie_name=movie_name

average_rating=total_rating_sum/movies_count

print(f'{max_rating_movie_name} is with highest rating: {max_rating:.1f}')
print(f'{min_rating_movie_name} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')