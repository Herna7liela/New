gbfile = open('sequence.gb', 'r')
read_gbfile = gbfile.readlines()
#print (read_gbfile)

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
#print (locus) # can divide up this part to get various inner parts

definition = read_gbfile[1][12:] + read_gbfile[2][12:]
#print (definition)

accession = read_gbfile[3][12:]
#print (accession)

version = read_gbfile[4][12:21]
#print (version) # is it neccessary to split these two???

gi = read_gbfile[4][22:]
#print (gi)
#
keywords = read_gbfile[5][12:]
#print (keywords)

source = read_gbfile[6][12:]
#print (source)
# organism is part of the source = look at the paper
organism = read_gbfile[7][12:] + read_gbfile[8][12:] + read_gbfile[9][12:] + read_gbfile[10][12:]
#organism = organism.split(";")
#print (organism) # not happy with this


content ={}
keys = ["Locus", "Definition", "Accession", "Version", "Keywords", "Source", "Organism"]
#pos = 0
#count = 0
#for key in keys:
    #basic_info = {}
    ##basic_info["Locus"] = read_gbfile[count][0:11]
    
    #if key == read_gbfile[count][0:11].rstrip():
        #content[key] = read_gbfile[count-1][12:] + read_gbfile[count][12:]
        #basic_info += key[pos]
        #pos += 1
        #count += 1
    #elif key[pos] == read_gbfile[count][12:]:
        #print (key[pos])
        #basic_info += key[pos]
        #pos += 1
        #count += 1    
#print (basic_info)

#info = {}
#count = 0
#key = read_gbfile[0][0:12].strip()
#while key != "REFERENCE":
    #gbfile = read_gbfile[0:]
    #print (gbfile)
    #content = read_gbfile[count][12:]
    #info[key] = content
### need to enter conditions for each of the keys because they differ
    ## need to find conditions for these functions to be right
    #if key == "LOCUS":
        #content = read_gbfile[count][12:].split(" ")
        #print (info["LOCUS"])
    #elif key == "DEFINITION":
        #content = read_gbfile[count][12:] + read_gbfile[count+1][12:]
        #print (info["DEFINITION"])
    
    #count += 1
    #key = read_gbfile[count][0:12].strip()
    
#print (info)

#Setting up the basic_info dictionary:
for line in read_gbfile:
    if line.startswith("LOCUS"):
        locus_info = line.split()
        locus = locus_info[1]
        dna_length = locus_info[2] + locus_info[3]
    if line.startswith("DEFINITION"):
        def_info = line.split()[1:]
        def_info = ' '.join(def_info)
        definition = def_info # how do I add the line after it in as well?
    if line.startswith('ACCESSION'):
        accession = line.split()[1]
    if line.startswith('SOURCE'): # also has an organism part and this must also come in here
        source_info = line.split()[1:]
        source_info = ' '.join(source_info)
        source = source_info # source and organism NB!!!
    elif line.startswith('REFERENCE'):
        pass
#print(locus, dna_length, definition, accession, source)

##genbank_info = [] # can use this list to put in all the dictionaries at the end of sorting out the structure. 
genbank = {}
genbank["LOCUS"] = locus
genbank["DNA_LENGTH"] = dna_length
genbank["DEFINITION"] = definition
genbank["ACCESSION"] = accession
genbank["SOURCE"] = source

print (genbank)

# is it neccessary to put all the info underneath the above in as well?
## also ask olivier to explain the stuff he said about the sys and os things

# can start here with an elif for the features if it will be understandable or with another if? but this depends
# on how to break the dicts up

# maybe something in the lines of the following:

#def over_lines(new_position, pattern='REFERENCE', ref1=2, ref2=3, space_used=12):
    #possible_dict = {pattern:[]}
    #if line.startswith(pattern):
        #pat_value = line.split()
        #pat_key = data[0]
        #if 'REFERENCE' in line:
            #reference_num = data[1]
            #possible_dict[pattern].append({'REFERENCE_NUM': reference_num})
            #ref_counter = 1
            #while (lines[possible_dict + ref_counter].startswith(' '*ref1)) or (lines[possible_dict + ref_counter].startswith(' '*ref2)):
                #possible_lines = lines[new_position + ref_counter]
                #tyd_key = possible_lines[:space_used].strip()
                #tyd_value = possible_lines[space_used:].strip()
                #ref_counter2 = 1
                #while lines[new_position+ ref_counter+ref_counter2].startswith(' '*space_used):
                    #tyd_line = ' '.join((lines[new_position+ref_counter+ref_counter2].split()[0:]))
                    
#tmpVal += ' ' + tmpLine #Otherwise space is truncated
#counter2 += 1
##It seems that an empty key is added.. Removed with if statement
#if tmpKey != '':
#if '/' in tmpVal:
#tmpVal = tmpVal.split('/')
##Add a map strip operation here
#currDict[pattern].append({tmpKey: tmpVal})
#counter1 += 1
##Record position of dict
#globList.append(currDict)
#return currDict
#filename = 'sequence.gb'
##Parsing the genbank file
#with open(filename) as handle:
##Try to consider multiple records, in a later dict implementation
#lines = handle.readlines()
#readSeq = False
#sequence = ''
##for line in read_gbfile:
    #if line.startswith('FEATURES'):
        #feat = read_gbfile(read_gbfile, pattern='FEATURES', ref1=5, ref2=5, space_used=21)
        #print (feat)
#for i in t['FEATURES']:
#print(i)
#if line.startswith('ORIGIN'):
#readSeq = True
#if (readSeq == True) and ('ORIGIN' not in line) and ('//' not in line):
#tmpSeq = line.strip().split()
#tmpSeq = tmpSeq[1:]
#tmpSeq = ''.join(tmpSeq)
    #sequence += tmpSeq