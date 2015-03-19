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