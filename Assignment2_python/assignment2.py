#go on uniprot and on faq programmatic access to get examples

# have to get this infomation into a structure like that of the movies
# divide it according to lines or tabulations or whatever the hell you can

# try make the ids the dictionary names into which you can then put the different sub ones

text = """
Entry	Gene names	Cross-reference (PDB)	Length
O95813	CER1 DAND4		267
Q8N907	DAND5 CER2 CKTSF1B3 GREM3 SP1		189
O60565	GREM1 CKTSF1B1 DAND2 DRM PIG2		184
P41271	NBL1 DAN DAND1	4X1J;	181
Q96S42	NODAL	4N1D;	347
Q15465	SHH	3HO5;3M1N;3MXW;	462"""



# the entry id can be used as the key and the rest as the values
# can look at for_loop exercises to see the tab example 006:...
morpho1 = {
    "ID" : "O95813",
    "Gene_names" : ["CER1, DAND4"],
    "PDB" : [""],
    "Length" : "267",   # try to arrange all the things like this and then compile movies = [mov1,mov2 etc] and then do questions
}

morpho2 = {
    "ID" : "Q8N907",
    "Gene_names" : ["DAND5, CER2, CKTSF1B3, GREM3, SP1"],
    "PDB" : [""],
    "Length" : "189",   
}

morpho3 = {
    "ID" : "O60565",
    "Gene_names" : ["GREM1, CKTSF1B1, DAND2, DRM, PIG2"],
    "PDB" : [""],
    "Length" : "184",   
}

morpho4 = {
    "ID" : "P41271",
    "Gene_names" : ["NBL1, DAN, DAND1"],
    "PDB" : ["4x1J"],
    "Length" : "181",   
}

morpho5 = {
    "ID" : "Q96S42",
    "Gene_names" : ["NODAL"],
    "PDB" : ["4N1D"],
    "Length" : "347",   
}

morpho6 = {
    "ID" : "Q15465",
    "Gene_names" : ["SHH"],
    "PDB" : ["3HO5, 3M1N, 3MXW"],
    "Length" : "462",   
}

morpho_genes = [morpho1, morpho2, morpho3, morpho4, morpho5, morpho6]
print (morpho_genes)


# 1. Create a function that returns the protein ID of the shortest protein.
#max_length = 500
#min_length = ""  

def shortest():
        lengthlist = sorted(morpho_genes, key=lambda i: i['Length'])
        shortestprotein = lengthlist[0]
        print("The shortest protein's ID is: ",shortestprotein["ID"])
shortest()

#def shortest(morpho_genes):  
        #while morpho_gene["Length"] < max_length:
                #min_length = min_length + Length
                #return min_length
#print (min_length,["Gene_name"])
        #for Length in morpho_genes:
            #min_length = min("Length")
            #return min_length
    #print (min_length)
        #for morpho in morpho_genes:
                #length = morpho["Length"]
                #shortest = min(length)
                #if shortest in length:     
                        #return morpho["ID"]
#print ("The shortest protein is ", shortest(morpho_genes))
# the output keeps giving where the function is saved in memory and not any data  



# 2. Create a function that receives a gene name and returns the protein ID. 
#def protID():
        #for morpho in morpho_genes:
                #gene_name = input("Enter a gene name to get it's protein ID: ")
                #if gene_name == morpho["Gene_names"]:
                        #return morpho["ID"]
                #print ("The ID corresponding the gene name is: ", ["ID"])

#protID()

def protID():
        gene_name = (input("Enter a gene name to find its protein ID: ")).lower()
        gene_list = ""
        while gene_name != "":
                for gename in morpho_genes:
                        gene_list = gename["Gene_names"]
                        if gene_name in gene_list:
                                print("T protein ID found for the ",gene_name,"was ", gename["ID"])
# gene_name = (input("Enter a gene name to continue or a blank line to stop: ")).lower()
protID()         

        
# 3. Create a function that receives protein ID and returns the PDB IDs. If the protein doesn’t have PDBs
# reported, the function should return False. 
#def pdbID(protID):
        #for morpho in morpho_genes:
                #protID = input("Enter the protein ID to find its PDB ID: ")
                #if morpho["PDB"] != "" in protID:
                        #return morpho["PDB"]
                #else:
                        #return False
#print (['PDB'], "if protein with ID ", pdbID(protID), "has PDB")

def pdbID():
        protID = input("Enter protein ID in order to get its PDB ID: ")
        pdbIDresults = morpho_genes[protID][1]
        if len(pdbIDresults[0]) == 0:
                return False
        else:
                return pdbIDresult
# dont know if this result is right because question 2 doesnt want to give a result???:(
pdbID()

# 4. Create a function that prints the proteins IDs and the number of reported genes. The list should be sorted
# by the number of genes. 
numbersorted = []
def sorted():
        for morpho in morpho_genes:
                numbersorted = morpho["Gene_names"].sort(len(morpho["Gene_names"]))
                numbersorted += numbersorted
                return numbersorted
print (["ID"] + numbersorted)
# this above function keeps saying numbersorted is not defined but it is defined inside the function
        

# 5. Create a function that prints a list of pairs of all the reported combinations of genes and PDBs
output = ()
def pairs():
        from itertools import combinations
        inputa = morpho["Gene_names"]
        inputb = morpho["PDB"]
        input = inputa + inputb
        output = sum([map(list, combinations(input, i)) for i in range(len(input) + 1)], [])
        output += output
        return output
pairs()
#def pairs():
        #print("Gene_name\tCross_ref_pdb")
#for item in list3:
#for item2 in item["Cross_ref_pdb"].split(";"):
#if item2!="":
#for item3 in item["Gene_name"].split():
#print(item3,'\t\t',item2)
#gene_names_paired_with_pdbs()


