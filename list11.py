# Write a program that asks the user for a number from 1 to 12, and then prints
# out the name of corresponding month, and the number of days in that month,
# in the form: "January has 31 days."

# it corresponds with question 4

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
number = int(input("Enter a number between 1 to 12: "))
print (months[number])
for number in months:
    if [number] % 2 == 0:
        print (number)
        
# needs more work