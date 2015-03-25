# Given a list of tuples each specifying a subject name and a grade symbol ('A' - 'F') in
# the form [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'),
# ('Science', 'B'), ('History', 'E')]:

##Write a program that prints out the subject with the highest mark.
grades = [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]

# can only take out symbols of the list
symbols = [x[1] for x in grades]
print (symbols)

# can find the index of "A"
indexsymbols = symbols.index('A')
print (indexsymbols)

# get the subject with symbol
#subsymbol = grades.index('A')
print grades[3]

# needs more work but preferrably do not use this type of method.
