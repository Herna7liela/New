# Write a program that reads a name and an age for a person, until the name is blank.
# As each name age pair is entered, store names in a list, and ages in another. Print a
# list of tuples of paired names and ages.

name = input("Enter name of person: ")
age = int(input("Enter age of same person: "))
pairs = (name,age)
namelist = ['']
agelist = ['']

if name != '':
    for pair in pairs:
        namelist = [namelist + (pair[0])]
        agelist = [agelist + (age[1])]
        print (namelist)
        print (agelist)
print (namelist, agelist)
