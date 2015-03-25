# Write a program that reads in names until a blank line is entered, and prints out each
# unique name and the number of times it was entered.

names = input("Enter a name: ")
listnames = {''}
counter = 0

for name in names:
        listnames = listnames + names
        counter = counter + 1
print (listnames)
print (counter)

# have to enter names
# then the names have to be in dictionary format
# then the names can be counted
# now how to print only the number of times a name was entered?