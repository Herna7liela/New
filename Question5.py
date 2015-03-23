# Based in the definition of the mathematical constant e, as the sum of an infinite
# series (see wikipedia: ​http://en.wikipedia.org/wiki/E_%28mathematical_constant%29)​
# create a program that ask the user for the number of terms used to calculate the
# approximation, and returns its value.


# because e is the sum of 1/factorial of a number n, I used the previous questions code.
number = int(input("Enter number to calculate contant e of: "))
fac = 1
i = 0
acc = 0
#while number != "":
for i in range(1,number+1):
        fac = fac*i
        #print(fac)
        for j in range(i):
                acc = acc + 1/(fac)
print (acc)
#number = int(input("Enter number to calculate contant e of: "))

# BEST WAY BELOW
# number_of_terms = int(input("how many terms? "))
# total = 1
# factorial = 1
# for counter in range(number_of_terms+1):
# factorial = factorial * (counter + 1)
#total = total + 1/factorial
# print("e= ", total)
        
   
    

