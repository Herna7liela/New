# Write a program that asks the user for a sequence of floats, ending in a blank line. The user is then allowed to give one of the following commands:
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
    elif numfloats == "":
        print ("Exiting program")
    numfloats = input("Enter a float: ")        

nummean = (total/count)
numsum = total        
print ("The mean of the entered floats are ", nummean)
print ("The sum of the entered floats are ", numsum)  
        
