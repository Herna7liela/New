
numbers = input("enter numbers")
smallnumber = 100000000000
while numbers != "":
    numbers = int(numbers)
    if smallnumber > numbers:
        smallnumber = numbers
        
    numbers = input("enter numbers")
    
print (smallnumber)


