import fresh_tomatoes
import media

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
                  
avatar = media.Movie("Avatar",
                     "A marie on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()


movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
