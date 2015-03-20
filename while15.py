# Write a program that asks the user for a sequence of floats, ending in a blank line.
# The user is then allowed to give one of the following commands:
#   mean: prints the mean of the numbers
#   sum: prints the sum of the numbers
#   quit: exits the program
#If 'mean' or 'sum' are entered, the program responds and then waits for more input.

numfloats = input("Enter a float: ")
total = 0
count = 0
while numfloats != "":
    if numfloats != "":
        numfloats = float(numfloats)
        total = total + numfloats
        count = count + 1  
    numfloats = input("Enter a float: ") 
    
nummean = (total/count)
numsum = total        
print ("The mean of the entered floats are ", nummean)
print ("The sum of the entered floats are ", numsum)      
      
for count in range(0:):           
    numfloats = input("Enter a float: ")
# use same idea as with average2.py, but 
# figure out a way to keep on repeating the things
#while numfloats != "":
#numfloats = input("Enter a float: ")
        
# so you have to be able to ask to print something and then get the value of it. 
# use a while loop to make it go on and on
# must put in something so that you can then ask the program to quite after which it
# will leave the while loop
# the while loop can only be exited when the condition is not met anymore