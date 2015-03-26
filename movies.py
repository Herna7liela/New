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
    "year":"2002",
    "actors":["Elijah Wood","Ian McKellen","Viggo Mortensen","Liv Tyler"]

}

movies = [movie1,movie2]
# can add more movies to the list

question = input("Do you want to enter another movie? (Y/N): ")
while question == "Y":
    movie = {}
    movie["name"] = input("Whats the name of the movie? ")
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
            actor = "" # dont use delete function because will then delete variable from function
            # we just reinitialized the variable by making it empty again
    if actor !="": # if it doesnt even go into the last else
        actors = actors + [actor] # this will add the very last one into the list
    
    movie["actors"] = actors
    
    movies += movie
    while question != "N" and question != "Y":
        question = input("Do you want to enter another movie? (Y/N): ")
    
print (movies)

# now we want to find a specific actor and that is why we put it in a list because there can be many movies
actor_q = input("Which actor should we look for? ")
answer = []
# go into list of movies
for movie in movies:
    # get the actors
    actors =  movie["actors"] # cannot access things in dictionary with numbers
    