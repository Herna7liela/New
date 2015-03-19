# Write a program that asks the user for two numbers and then prints the sum
# of numbers from the lowest number entered to the highest number entered.

a = int(input("Enter number: "))
b = int(input("Enter number: "))
total = a

if a <= b:
    for i in range(a, b):
        total = total + i
    print (total)


