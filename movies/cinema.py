from movies import media
from movies import fresh_tomatoes

print(media.Movie.__bases__)
print(media.Movie.__dict__)
print(media.Movie.__doc__)
print(media.Movie.__module__)
print(media.Movie.__name__)
print("==========")

avatar = media.Movie("Avatar", "An ex-Marine who finds himself thrust into hostilities on an alien planet filled with exotic life forms.",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49433", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.__dict__)
print(avatar.__class__)
print(avatar)
movies = [avatar]
fresh_tomatoes.open_movies_page(movies)
