# Write a program that prints the numbers from 1 to 100, 10 per each line.

for i in range(1,100):
    if i % 10 == 0:
        print(i)
    else:
        print (i, end = "")