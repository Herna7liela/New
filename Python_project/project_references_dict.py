gbfile = open('sequence.gb', 'r')
read_gbfile = gbfile.readlines()
print (read_gbfile)

refs = read_gbfile[11:]
print (refs)

## going to use refs to do the following code

ref1 = refs[0][12:14]
print (ref1)

authors1 = refs[1][12:]
print (authors1)

title1 = refs[2][12:] + refs[3][12:]
print (title1) # how can I print without making a new line?

journal1 = refs[4][12:]
print (journal1)

pubmed = refs[5][12:]
print (pubmed)

# this is only for the first reference. 
# have to find a way to loop over all of these and then to add in the other references
# ref2 and 3 will have the same format as the above
# use a counter in order to count the positions not the characters becuase the characters will probably stay
# constant
