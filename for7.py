# Write a program that asks the user for two numbers and then prints the sum
# of numbers from the lowest number entered to the highest number entered.

a = int(input("Enter number: "))
b = int(input("Enter number: "))
total = 0

while a <= b:
    for i in range(a, b):
        total = i +1
    print (total)


#i=int(input(“enter first number”)
#b=int(input(“enter second number”)
#total = 0
#while i<=b:
#total = tptal +i
#i=i+1
#print(total)