# going to work with movies: name, rating, actors, release year.
# name used as key of rest of information

movie1 = {
    "name":"The Grey",
    "rating": "79",
    "year":"2012",
    "actors":["Liam Neeson", "Frank Grillo", "Dermot Mulroney"]
}

movie2 = {
    "name":"LOTR:TFOTR",
    "rating":"91",
    "year":"2002"
    "actors":["Elijah Wood","Ian McKellen","Viggo Mortensen","Liv Tyler"]

}

movies = [movie1,movie2]
# can add more movies to the list

movie = {}
movie["rating"] = int(input("What is the rating? "))
movie["year"] = int(input("What is the year? "))
actors_str = input("Give list of actors (comma separated): ")
actor = ""
actors = []
for char in actors:
    if char!=",":
        actor = actor + char
    else:
        actors = actors + [actor]
movie["actors"] = 