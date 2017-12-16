from movies import media
from movies import fresh_tomatoes

avatar = media.Movie("Avatar", "An ex-Marine who finds himself thrust into hostilities on an alien planet filled with exotic life forms.",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49433", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
movies = [avatar]
fresh_tomatoes.open_movies_page(movies)
