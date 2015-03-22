# Based in the definition of the mathematical constant e, as the sum of an infinite
# series (see wikipedia: ​http://en.wikipedia.org/wiki/E_%28mathematical_constant%29)​
# create a program that ask the user for the number of terms used to calculate the
# approximation, and returns its value.


# because e is the sum of 1/factorial of a number n, I used the previous questions code.
number = float(input("Enter number to calculate contant e of: "))
fac = 1
i = 0
while number != "":
    for i in range(1,number,1):
        fac = fac*i
        print(fac)
    for i in range(1,number,1):
        print sum(1/float(fac))
        
   
    

