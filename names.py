# Write a program that asks the user for a list of names ending with a blank line. 
# program then outputs a neat list containing the following, each on their own line,
# labelled: The first name alphabetically. The last name alphabetically, the shortest name,
# and the longest name.

name = input("Type in a name: ")
count = 1                                

while name != "":
                                # put in a function that places all the inputs in a list
    if name == min(name):       # have to be able to keep the shortest
        shortest = min(name)
    elif name == max(name):
        longest = max(name)                          # if name == min(name)
    else:
        snames = sorted(names)                       #    min.name[counter] = min(name)

    count = count + 1
    names = 
                                
                                # get all input names in one variable
print (sort(name))               
print ("The shortest name is ", shortest) 
print ("The longest name is ", longest)
