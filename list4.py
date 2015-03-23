# Write a program that asks the user to enter a number from 1 to 12 and
# prints out the name of the corresponding month.

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#months = [January, February, March, April, May, June, July, August, September, October, November, December]
number = int(input("Enter a number between 1 to 12: "))
print (months[number])