#f = open('sequence.gb', 'r')


#print (f.readlines())

#import sys
#print (sys.argv)

# can put the last line in the first to be able to make it achievable everywhere

gbfile = open('sequence.gb', 'r')
read_gbfile = gbfile.readlines()
#print (read_gbfile)

#def normalize_space(read_gbfile):
    ##Return s stripped of leading/trailing whitespace and with internal runs of whitespace replaced by a single SPACE
    #return ' '.join(read_gbfile.split())
#new_gb = [normalize_space(i) for i in read_gbfile]
##print (new_gb)

#basic = new_gb[0:11]
##print (basic) # this to to get everything up until refs

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

#print (genbank)


# References and features and the sequence have to come in first before this
#R:References S:Sequence M:Motif T:Translate F:Features E:Export Q:Quit
#Codon table
import sys, os, re
from urllib import sys
codon_table = {}
print ("Need to safe codon table from link in text file called codon_table.txt: https://popoolation.googlecode.com/svn-history/r179/trunk/syn-nonsyn/codon-table.txt")
url = "https://popoolation.googlecode.com/svn-history/r179/trunk/syn-nonsyn/codon-table.txt" # this is the url the table was from
if not os.path.exists("./codon_table.txt"):
    urlpage = request.urlopen(url)
    urlpage = urlpage.read().decode("utf8")
    for line in urlpage.split("\n"): # splitting things according to what is in the webpage
        if not line.startswith("#"):
            codon, aa = line.split(":")
            codon_table[codon] = aa.lstrip()
        else:
            url_handle = open("codon_table.txt",'r')
            url_page = url_handle.readlines()
            for line in purl_age:
                if not line.startswith("#"):
                    line = line.rstrip()
                    codon, aa = line.split(":")
                    codon_table[codon] = aa.lstrip()

                    gbfile = open("sequence.gb", 'r')
                    read_gbfile = gbfile.readlines()
                    print (read_gbfile)
                    
                    

                
#maybe something in the lines of the following:
complete_list = []
def over_lines(new_position, pattern = "REFERENCE", ref1 = 2, ref2 = 3, space_used = 12): # olivier explained the ref1 and ref2 part
    possible_dict = {pattern:[]}
    if line.startswith(pattern):
        pat_value = line.split()
        pat_key = pattern[0] # i had a variable called data but it said its not defined
        if "REFERENCE" in line:
            reference_num = pattern[1]
            possible_dict[pattern].append({"REFERENCE_NUM": reference_num})
            ref_counter = 1
            while (lines[possible_dict + ref_counter].startswith(' '*ref1)) or (lines[possible_dict + ref_counter].startswith(' '*ref2)):
                # above line have problems with int and dict to combine it
                possible_lines = lines[new_position + ref_counter]
                tyd_key = possible_lines[:space_used].strip()
                tyd_value = possible_lines[space_used:].strip()
                ref_counter2 = 1
                while lines[new_position + ref_counter + ref_counter2].startswith(' '*space_used):
                    tyd_line = " ".join((lines[new_position + ref_counter + ref_counter2].split()[0:]))
                    tyd_value += " " + tyd
                    ref_counter2 += 1
                    #for some reason an empty key was added here so have to remove it.
                    if tyd_key != "":
                        if "/" in tyd_value:
                            tyd_value = tyd_val.split("/")
                            tyd_value = list(map(lambda x: x.strip(), tyd_value))
                            for m, n in enumerate(tyd_value):
                                if "translation" in n:
                                    n = n.replace(" ", "")
                                    tyd_value[m] = n
                            possible_dict[pattern][tyd_key] = tyd_value
                            ref_counter += 1
                            #Record position of dict. Maybe add it to the object somewhere around here?
                            genbank.append(possible_dict)                            
#print (genbank)


#Record position of dictionary in order to designate a specific position in the memory
#genbank.append(possible_dict)
#return possible_dict
genbank_file = "sequence.gb"
#Parsing the genbank file
with open(genbank_file) as handle:
    lines = handle.readlines()
    read_genseq = False

def features_thingy():
    if line.startswith("FEATURES"): # it keeps on saying here that the line is not defined, but I dont get why not?
        genbank["FEATURES"] = read_gbfile(read_gbfile, pattern = "FEATURES", ref1 = 5, ref2 = 5, space_used = 21)
        #print (features) ## to see if the right thing prints
    #for i in genbank["FEATURES"]:
        #print(i)
        if line.startswith("SOURCE"):
            read_gbSeq = True
            if (read_gbSeq == True) and ("ORIGIN" not in line) and ("//" not in line): # this looks very confusing to me but it does make sense
                tyd_gbSeq = line.strip().split()
                tyd_gbSeq = tyd_gbSeq[1:]
                tyd_gbSeq = "".join(tyd_gbSeq)
                sequence += tyd_gbSeq
                pass
            genbank["ORIGIN"] = sequence
#print (genbank["ORIGIN"])  

def reference_thingy(): # olivier told me to add in a reference handler so I put it in a function in order to call it later on
    # but I then also combined the handler with being able to call the M command in the terminal and get an output = this 
    # I did becuase I wasnt completely sure what he meant by the handler but I still kept the name as is
    number_references = 0
    authors = []
    titles = []
    journal = ""
    for dictionary in genbank:
        if list(dictionary.keys())[0] == "REFERENCE":
            number_references += 1
            authors.append(dictionary["REFERENCE"]["AUTHORS"])
            titles.append(dictionary["REFERENCE"]["TITLE"])
            journal += dictionary["REFERENCE"]["JOURNAL"]
            #print('Just to test the dictionary: ', dictionary)
            print("There are", number_references, "articles reported for this sequence", accession)
            for idx, author in enumerate(authors):
                print("[" + str(idx + 1) + "]", author)
                reference_details = input("Input the number of the reference for details (M for the Menu): ")
                if reference_details == "M":
                    return "Continue"
                else:
                    reference_details = int(reference_details)
                    print("Title:\n\t" + titles[reference_details - 1])
                    print("Authors")
                    few_auth = authors[reference_details - 1].replace(".,", ".").replace(" and ", " ").split(" ")
                    for auth in few_auth:
                        print("\t" + auth)
                        print("Journal:\n\t" + journal)
                        M_command = input("Input the number of the reference for details (M for the Menu): ")
                        if M_command == "M":
                            return "Continue"
                        return None
                    class Genbank: # ask eggies again for why I had to put this in here???
                        ##Container for genbank record # conatiner idea from egbert and he also told me to use _init_
                        def __init__(gb, sequence, references, features, accession, length):
                            gb.sequence = sequence
                            gb.reference = reference
                            gb.features = features
                            gb.accession = accession
                            gb.length = length                        

def translate_nucl_seq(gb, frame = 0):
    gb.sequence = gb.sequence[frame:]
    sequence_len = len(gb.sequence)
    protein = ""
    codons = [gb.sequence[i: i + 3] for i in range(0, sequence_len -3 + 1, 3)]
    for codon in codons:
        yaay = codon_table[codon]
    # took out the stop codon because it didnt look nice and also didnt make sense
        if yaay == "-":
            break
        else:
            new_protein += yaay
            return new_protein
    
def sequence_thingy(): 
    seq_range = input("Enter chosen range: ")
    if seq_range == "M":
        return "Continue"
    else:
        left = seq_range[0]
        right = seq_range[-1]
        seq_range = seq_range[1: - 1].split(",")
        lower_limit = int(seq_range[0])
        upper_limit = int(seq_range[1])
## to correct the limits becuase its off
    if left == "(":
        lower_limit += 1
    elif left == "[":
        lower_limit -= 1 # I thought the minus would work in the same way as the +
    if right == ")":
        upper_limit -= 1
    elif right == "]":
    #Include this limit
        pass
    
    for dictionary in genbank:
        if list(dictionary.keys())[0] == "SEQUENCE":
            possible_sequence = dictionary["SEQUENCE"][lower_limit: upper_limit].upper()
    for i in range(0,len(possible_sequence), 60):
        print(possible_sequence[i: i + 60])
        return None

def motif_thingy():
    pass
name = "sequence.gb"
#Parsing the gb file
with open(name) as gbmot:
    lines = gbmot.readlines()
    gbot_len = len(lines)
    read_sequence = False
    sequence = ""
    running = True
while running:
    for lineIdx, line in enumerate(lines): # egbert helped with this part to be able to take everything together
        if line.startswith("LOCUS"):
            locus_information = line.split()
            locus = locus_information[1]
            length = locus_information[2] + locus_information[3]
        elif line.startswith("ACCESSION"):
            accession = line.split()[1]
        elif line.startswith("SOURCE"):
            source_description = line.split()[1:]
            source_description = " ".join(source_description)
            source = source_description
        elif line.startswith("REFERENCE"):
            over_lines(lineIdx, pattern = "REFERENCE")
        elif line.startswith("FEATURES"):
            over_lines(lineIdx, pattern = "FEATURES", ref1 = 5, ref22 = 5, space_used = 21)
        elif line.startswith('ORIGIN'):
            read_sequence = True
            if (read_sequence == True) and ('ORIGIN' not in line) and lineIdx <= gbmot_len: #Careful of the record separator
                possible_sequence = line.strip().split()
                possible_sequence = possible_sequence[1:]
                possible_sequence = "".join(possible_sequence)
                sequence += possible_sequence
                genbank.append({"SEQUENCE": sequence})
                read_sequence = False 
                sequence = "" #Re-initialise sequence
                l1 = "GBK Reader - (" + filename +") DNA"
                l2 = "="*70
                l3 = "Sequence: " + accession + " (" + locus + ", " + length + ")"
                l4 = "Description: " + description
                l5 = "Source: " + source
                l6 = "Number of References", None
                l7 = "Number of Features", None
                l8 = "="*70
#print(l1)
#print(l2)
#print(l3)
#print(l4)
#print(l5)
#print(l6)
#print(l7)
#print(l8)
#print()


## need to call the right functions with this part!!!!
user_input = input("Enter one of the following options: R:References S:Sequence M:Motif T:Translate F:Features E:Export Q: Quit\n>: ")
if user_input == "Q":
    running = False
elif user_input == "R":
#Do reference stuff
    if reference_thingy() == "Continue":
        pass # kept saying that the "Continue" was not properly in the loop
elif user_input == "S":
#Do sequence stuff
    if sequence_thingy() == "Continue":
        pass # changed most continue to pass to be able to keep running the function because the continue kept saying it was nt in the loop
elif user_input == "M":
    if motif_thingy() == "Continue":
        motifPrompt = input("Motif: ")
        while len(motifPrompt) < 5:
            motifPrompt = input("Motif: ")
            print("Searching for the motif ", motifPrompt.lower() + "...")
            pass
elif user_input == "T":
    if translate_nucl_seq(gb, frame = 0) == "Continue":
        pass
elif user_input == "F":
    if features_thingy() == "Continue":
        pass
elif user_input == "E":
    # find a way to export the gbk file into fasta format
    
    ## the export can be done by using biopython by using the following
    # from Bio import SeqIO
    #record = SeqIO.read("yourGenbankFileDirectory/yourGenbankFile.gb","genbank")
    #rawSequence = record.seq.tostring()
    #nameSequence = record.features[0].qualifiers
    #from Bio import SeqIO
    #record = SeqIO.read("yourGenbankFileDirectory/yourGenbankFile.gb","genbank")
    #rawSequenceList = [gene.extract(record.seq.tostring()) for gene in record.features]
    #nameSequenceList = [gene.qualifiers for gene in record.features]
    
    ## still need a manual way of doing this
    pass
elif user_input == "":
    print(genbank)
