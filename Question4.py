# Create a program that calculates the factorial of a number n entered by the user.
# For example the factorial of 5:

# make a function that multiplies the number by itself as well as with all the
# numbers lower that it

number = int(input("Enter number to calculate factorial of: "))
ans = 1

for i in range(1,number+1,1):
        ans = ans*i
        print(ans)
