# Same as above, except now with the right angle in the top right! Example ...

#Enter triangle height: 3
#***
# **
#  *
height = int(input("Enter triangle height: "))
count = height
space = 0
# height != "":
for i in range(1,height+1):
    #print (i)
    count = count - 1
    #print (count*'*')
    space = space + 1
    print (' '*space + count*'*')
    #height = int(input("Enter triangle height: "))
