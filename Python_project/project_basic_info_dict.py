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

genbank = {}
#Setting up the basic_info dictionary:
for line in read_gbfile:
    if line.startswith("LOCUS"):
        locus_info = line.split()
        locus = locus_info[1]
        dna_length = locus_info[2] + locus_info[3]
    if line.startswith("DEFINITION"):
        genbank["DEFINITION"] = line[12:].rstrip()
        def_key = line[0:11].strip()
    if line.startswith('ACCESSION'):
        accession = line.split()[1]
    if line.startswith('SOURCE'): # also has an organism part and this must also come in here
        #can possibly use the code from definition to get the organism in here as well
        source_info = line.split()[1:]
        source_info = ' '.join(source_info)
        source = source_info 
    if line.startswith("        "):
        genbank[def_key] = genbank[def_key] + line.strip()
    elif line.startswith('SOURCE'):
        break
#print(locus, dna_length, definition, accession, source)

##genbank_info = [] # can use this list to put in all the dictionaries at the end of sorting out the structure. 
genbank["LOCUS"] = locus
genbank["DNA_LENGTH"] = dna_length
genbank["ACCESSION"] = accession
genbank["SOURCE"] = source

print (genbank)


