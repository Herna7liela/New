gbfile = open('sequence.gb', 'r')
read_gbfile = gbfile.readlines()
print (read_gbfile)


## still have to ask olivier to explain the stuff he said about the sys and os things when calling the program in the terminal

#maybe something in the lines of the following:
complete_list = []
def over_lines(new_position, pattern='REFERENCE', ref1=2, ref2=3, space_used=12): # olivier explained the ref1 and ref2 part
    possible_dict = {pattern:[]}
    if line.startswith(pattern):
        pat_value = line.split()
        pat_key = data[0]
        if 'REFERENCE' in line:
            reference_num = data[1]
            possible_dict[pattern].append({'REFERENCE_NUM': reference_num})
            ref_counter = 1
            while (lines[possible_dict + ref_counter].startswith(' '*ref1)) or (lines[possible_dict + ref_counter].startswith(' '*ref2)):
                possible_lines = lines[new_position + ref_counter]
                tyd_key = possible_lines[:space_used].strip()
                tyd_value = possible_lines[space_used:].strip()
                ref_counter2 = 1
                while lines[new_position+ ref_counter+ref_counter2].startswith(' '*space_used):
                    tyd_line = ' '.join((lines[new_position+ref_counter+ref_counter2].split()[0:]))
                    tyd_value += ' ' + tyd
                    ref_counter2 += 1
                    #for some reason an empty key was added here so have to remove it.
                    if tyd_key != "":
                        if "/" in tyd_value:
                            tyd_value = tyd_val.split("/")
                            tyd_value = list(map(lambda x: x.strip(), tyd_value))
                            for m, n in enumerate(tyd_value):
                                if 'translation' in n:
                                    n = n.replace(' ', '')
                                    tyd_value[m] = n
                            possible_dict[pattern][tyd_key] = tyd_value
                            ref_counter += 1
                            #Record position of dict. Maybe add it to the object somewhere around here?
                            genbank.append(possible_dict)                            
#print (genbank)


#Record position of dictionary in order to designate a specific position in the memory
#genbank.append(possible_dict)
#return possible_dict
genbank_file = 'sequence.gb'
#Parsing the genbank file
with open(genbank_file) as handle:
    lines = handle.readlines()
    read_genseq = False
if line.startswith("FEATURES"): # it keeps on saying here that the line is not defined, but I dont get why not?
    genbank["FEATURES"] = read_gbfile(read_gbfile, pattern='FEATURES', ref1=5, ref2=5, space_used=21)
    #print (features) ## to see if the right thing prints
#for i in genbank["FEATURES"]:
    #print(i)
    if line.startswith("SOURCE"):
        read_gbSeq = True
        if (read_gbSeq == True) and ("ORIGIN" not in line) and ('//' not in line): # this looks very confusing to me but it does make sense
            tyd_gbSeq = line.strip().split()
            tyd_gbSeq = tyd_gbSeq[1:]
            tyd_gbSeq = ''.join(tyd_gbSeq)
            sequence += tyd_gbSeq
            pass
        genbank["ORIGIN"] = sequence
print (genbank["ORIGIN"])  

def reference_andler(): # olivier told me to add in a reference handler so I put it in a function in order to call it later on
    # but I then also combined the handler with being able to call the M command in the terminal and get an output = this 
    # I did becuase I wasnt completely sure what he meant by the handler but I still kept the name as is
    number_references = 0
    authors = []
    titles = []
    journal = ''
    for dictionary in genbank:
        if list(dictionary.keys())[0] == 'REFERENCE':
            number_references += 1
            authors.append(dictionary['REFERENCE']['AUTHORS'])
            titles.append(dictionary['REFERENCE']['TITLE'])
            journal += dictionary['REFERENCE']['JOURNAL']
            #print('Just to test the dictionary: ', dictionary)
            print('There are', number_references, 'articles reported for the sequence', accession)
            for idx, author in enumerate(authors):
                print('['+str(idx+1)+']', author)
                reference_details = input('Input the number of a reference for details (M for the Menu) :')
                if reference_details == 'M':
                    return 'continue'
                else:
                    reference_details = int(reference_details)
                    print('Title:\n\t'+titles[reference_details - 1])
                    print('Authors')
                    few_auth = authors[reference_details - 1].replace('.,', '.').replace(' and ', ' ').split(' ')
                    for auth in few_auth:
                        print('\t' + auth)
                        print('Journal:\n\t'+journal)
                        M_command = input('Input the number of a reference for details (M for the Menu) :')
                        if M_command == 'M':
                            return 'continue'
                        return None