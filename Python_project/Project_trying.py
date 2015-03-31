# STEP 1:
# get the file in the correct format .gb to be able to work with it
# have to start by opening a a reader. The file to open is the argument to the python program
# python3 Project_final_code.py file.gb (use the sys.argv function after importing sys)

# STEP 2:
# get the .gb file content into exp text = "...."
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
print (basic)
dict_exam={}

intro = basic[0].split(" ")
if "LOCUS" == intro[0]:
    dict_exam[intro[0]] = intro[1:]

intro = basic[1].split(" ")
if "DEFINITION" == intro[0]:
    dict_exam[intro[0]] = basic[1][11:]

intro = basic[2].split(" ")
if "ACCESSION" == intro[0]:
    dict_exam[intro[0]] = basic[2][11:]

print (dict_exam)

#count = 0
#new_pos = 1
#for content in intro:
    #dict_exam = {}
    #if intro == basic[count].split(" "):
        #if key == intro[count]:
            #dict_exam[intro[count]] = basic
#basic_info = []
#for content in intro:
    ## print (content)
    #dic = {}
    #dic["Locus"] = content[1]
    #dic["Length"] = content[2:4]
    #dic["Type_nucl"] = content[4:7]
    ##dic["Submit_date"] = content[]
    #basic_info += [dic]
#print (basic_info)    

    


#for content in new_gb:
 #   print (content)
 


#definition = read_gbfile[1:3]
#print(definition)
#accession = read_gbfile[3]
#print ([accession])
#GI = read_gbfile[4]
#print (GI)


## try to possible get the script of how to parse files with biopython!!!!
## look at bioparsers and biogenbank
# set up functions so long for R, S, M, T, F, E, Q
# can then add the contents of the functions to the set up functions later on

# STEP 3:
# 

# create a regular expression
# use the pipe 
# import module from builtin re and then search for expression
# use re.compile to create the expression that will search for the expression