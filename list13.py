# Write a program that asks the user for the height of a triangle. If a blank line
# is entered, the program finishes, otherwise it prints out a right handed triangle,
# with the right angle on the bottom right, made of asterisks ('*') of a height equal
# to the number entered. Example input/output follows ...
#Enter triangle height: 3
#*
#**
#***

height = int(input("Enter triangle height: "))
count = 0
# height != "":
for i in range(1,height+1):
                #print (i)
                count = count + 1
                print (count*'*')
                #height = int(input("Enter triangle height: "))
                
# need to get a way for the loop to keep going until a blank line is entered.
                
                                                                                         

