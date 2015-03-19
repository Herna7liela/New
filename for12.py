# Write a program that prints the numbers from 1 to 100, 10 per each line.

counter = 0
for i in range(1,100):
            if counter == 5:
                        counter = 0
                        print i
            else:
                        print i,
counter = counter + 1    