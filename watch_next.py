import difflib


def similar_movie(description):
    with open("movies.txt", "r") as m:
        movies = m.readlines()

    match = difflib.get_close_matches(description, movies, n=1)
    if match:
        for movie in match:
            title = movie.split(':')[0].strip()
        return title
    else:
        return "no similar movie found"


description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = similar_movie(description)
print("You should watch", similar_movie, "next.")
