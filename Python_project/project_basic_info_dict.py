gbfile = open('sequence.gb', 'r')
read_gbfile = gbfile.readlines()
print (read_gbfile)

# set up a structure to be able to answer questions

def normalize_space(read_gbfile):
    #Return s stripped of leading/trailing whitespace and with internal runs of whitespace replaced by a single SPACE
    return ' '.join(read_gbfile.split())
new_gb = [normalize_space(i) for i in read_gbfile]
#print (new_gb)

basic = new_gb[0:11]
#print (basic) # this to to get everything up until refs


## the below code is if I use the normalized space code also        
#locus = basic[0][6:]
#print (locus) # can divide up this part to get various inner parts

#definition = basic[1][11:] + basic[2]
#print (definition)

#accession = basic[3][10:]
#print (accession)

#version = basic[4][8:17]
#print (version)

#gi = basic[4][20:]
#print (gi)

#keywords = basic[5][9:]
#print (keywords)

#source = basic[6][7:]
#print (source)

#organism = basic[7][9:] + basic[8] + basic[9] + basic[10]
#organism = organism.split(";")
#print (organism) # not happy with this


## now using the read_gbfile before the spaces were normalized
locus = read_gbfile[0][12:]
print (locus) # can divide up this part to get various inner parts

definition = read_gbfile[1][12:] + read_gbfile[2][12:]
print (definition)

accession = read_gbfile[3][12:]
print (accession)

version = read_gbfile[4][12:21]
print (version) # is it neccessary to split these two???

gi = read_gbfile[4][22:]
print (gi)

keywords = read_gbfile[5][12:]
print (keywords)

source = read_gbfile[6][12:]
print (source)
# organism is part of the source = look at the paper
organism = read_gbfile[7][12:] + read_gbfile[8][12:] + read_gbfile[9][12:] + read_gbfile[10][12:]
#organism = organism.split(";")
print (organism) # not happy with this


