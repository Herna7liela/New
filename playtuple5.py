grades = [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]

# this is tuples within a list
# to get word 'French' out of list and go straight into french
grade[3]
# to get french out
grade[3][0]
# first index is higher structure and second index is lower structure
# going deeper in
grade[3][0][3]
# this will start giving you a letter and not a string

# for loop can deal with anything so use it
# think in stages with a for loop because this gives each item at a time
# for loop goes trough a list

# see something as a list: list(range(0,100))
for item in range (100):
# for will go here from 1 to 100 is steps of 1.

list = [3,4,5,3,2,2,6,5,4]
counter = 0
for item in list:
    print (item)
    counter = counter +1
    
list
for i in [0,1,2]:
    print (list(i))
    
# is length of my list is very long then:
for i in range(3):
    print (list(i))
# because i is an artificail thing

# if you dont know how long something is:
len(list)
# can then say by adding different inputs into one
for i in range(len(list)):
    print (list(i))
    
for item in list:
    print (item)
    # but this doesnt have a counter so cant get position like in the previous example

# can then say:
print (list[1]) # where you will only print the item on position 1 and not zero.
# or
print (i,list[i]) # to use position to get to other position

for counter in range(len(grades)):
    print (counter) # to just keep track of positions in the whole list of just the counter
    print (grades[counter]) # counter used to keep track of positions of the whole list
    print (grades[counter][1]) # to only print the grades
    
for grade in grades:
    for item in grade:
        print (item) # this goes inside then inside then inside etc...
        
        