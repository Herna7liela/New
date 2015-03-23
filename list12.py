# Modify your answer to question 10 from "Flow Control: Conditionals", i.e.
# print out the numbers from 1 to 10 by which a user entered number is divisible,
# to use a for loop instead of multiple if statements.

for i in range(1,10):
    print (i)
    number = int(input("Enter number to divide by: "))
    if i % number == 0:
        print (i)
        
# need more work