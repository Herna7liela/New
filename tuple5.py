# Given a list of tuples each specifying a subject name and a grade symbol ('A' - 'F') in
# the form [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'),
# ('Science', 'B'), ('History', 'E')]:

##Write a program that prints out the subject with the highest mark.
#Write a program that outputs each subject and the grade symbol in the format 'subject: symbol', with each subject on a single line.
## Write a program that prints out a tab separated list of subjects on the first line, and
# the corresponding grades, also tab separated on the second line.

grades = [('Maths', 'D'), ('Comp Sci', 'B'), ('English', 'C'), ('French', 'A'), ('Science', 'B'), ('History', 'E')]
lowgrade = ('XXX','Z')
for grade in grades: 
    if lowgrade[1] > grade[1]:
        lowgrade = grade
print (lowgrade)
    #new = grades.sorted[1]
    #print (new)
    #print (grade[0], grade[1])
    
#    print (new)
