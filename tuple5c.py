# Write a program that prints out a tab separated list of subjects on the first line, and
# the corresponding grades, also tab separated on the second line.

grades = [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]

for grade in grades:
    print (grade[0], end = '\t')
print ()

for grade in grades:    
    print (grade[1], end = '\t')
print ()
    #print (grade[1])