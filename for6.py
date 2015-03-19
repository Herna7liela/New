# Write a program that asks the user for a number and then prints the sum
# of numbers from 1 to the number they entered.

number = int(input("Enter number: "))
total = number

for i in range(1, number):
    total = total + i
    print (total)