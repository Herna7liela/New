# Modify your solution to question 10 so that instead of printing the average
# and then terminating when a blank line is entered, it prints the average and
# then asks if the user wants to repeat the process. If the user answers 'y' the
# process is repeated, otherwise the program terminates.

numbers = input("enter numbers ")
total = 0
count = 0
while numbers != "":
    numbers = int(numbers)
    total = total + numbers
    count = count + 1
    
    numbers = input("enter numbers ")

average = (total/count)
        
print (average)