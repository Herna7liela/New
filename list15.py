# Write a program that prints out a 'Christmas' tree shape from asterisks.
# The program should ask the user for the height of the tree, in lines, and
# the tree should have a stalk of two lines regardless. If the user enters a height,
# the tree should be printed out, and the user should be prompted for another height
# until they enter a blank line.

#Enter tree height: 4
#   *
#  ***
# *****
#*******
#   *
#   *
height = int(input("Enter triangle height: "))
count = 0
space = height 
# height != "":
for i in range(1,height+1):
    count = count + 1
    space = space - 1
    print (space*' ' + count*'*', end = "")
    print ((count-1)*'*' + space*' ')
    
    
print ((height -1 )* " " + '*')
print ((height -1 )* " " + '*')
