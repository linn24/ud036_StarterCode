import media
import fresh_tomatoes

# instantiate movies
pitch_perfect = media.Movie(
                "Pitch Perfect",
                "https://upload.wikimedia.org/wikipedia/en/b/b9/Pitch_Perfect_movie_poster.jpg",
                "https://www.youtube.com/watch?v=8dItOM6eYXY")

black_pearl = media.Movie(
            "The Black Pearl",
            "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
            "https://www.youtube.com/watch?v=naQr0uTrH_s")

dead_man = media.Movie(
    "Dead Man's Chest",
    "https://upload.wikimedia.org/wikipedia/en/2/2d/Pirates_of_the_caribbean_2_poster_b.jpg",
    "https://www.youtube.com/watch?v=ozk0-RHXtFw"
    )

world_end = media.Movie(
    "At World's End",
    "https://upload.wikimedia.org/wikipedia/en/5/5a/Pirates_AWE_Poster.jpg",
    "https://www.youtube.com/watch?v=HKSZtp_OGHY"
    )

stranger_tides = media.Movie(
    "On Stranger Tides",
    "https://upload.wikimedia.org/wikipedia/en/c/c6/On_Stranger_Tides_Poster.jpg",
    "https://www.youtube.com/watch?v=KR_9A-cUEJc"
    )

tell_no_tales = media.Movie(
    "Dead Men Tell No Tales",
    "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
    "https://www.youtube.com/watch?v=a5V5C8mEVzY"
    )

# create a list of movies
movies = [pitch_perfect, black_pearl, dead_man, world_end, stranger_tides, tell_no_tales]

# display movies on the page
fresh_tomatoes.open_movies_page(movies)



