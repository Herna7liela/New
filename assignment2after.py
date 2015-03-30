text = """Entry	Gene names	Cross-reference (PDB)	Length
O95813	CER1 DAND4		267
Q8N907	DAND5 CER2 CKTSF1B3 GREM3 SP1		189
O60565	GREM1 CKTSF1B1 DAND2 DRM PIG2		184
P41271	NBL1 DAN DAND1	4X1J;	181
Q96S42	NODAL	4N1D;	347
Q15465	SHH	3HO5;3M1N;3MXW;	462"""

newlist = text.split("\n")
#print (newlist)

newlist2 = newlist[1:]
#print(newlist2)

newlist3 = []
morpho = []
for item in newlist2:
    #print (item)
    #print (item.split('\t'))
    morpho = item.split('\t')
    newlist3 += [morpho]
#print (newlist3)

newlist4 = []

for content in newlist3:
    #print (content)
    dic = {}
    dic["Entry"] = content[0]
    dic["Gene_names"] = content[1].split()
    dic["PDB ID"] = content[2].split(';')
    dic["Length"] = content[3]
    newlist4 += [dic]
#print (newlist4)

# [{'Entry': 'O95813', 'Length': '267', 'Gene_names': 'CER1 DAND4', 'PDB ID': ''}, {'Entry': 'Q8N907', 'Length': '189', 'Gene_names': 'DAND5 CER2 CKTSF1B3 GREM3 SP1', 'PDB ID': ''}, {'Entry': 'O60565', 'Length': '184', 'Gene_names': 'GREM1 CKTSF1B1 DAND2 DRM PIG2', 'PDB ID': ''}, {'Entry': 'P41271', 'Length': '181', 'Gene_names': 'NBL1 DAN DAND1', 'PDB ID': '4X1J;'}, {'Entry': 'Q96S42', 'Length': '347', 'Gene_names': 'NODAL', 'PDB ID': '4N1D;'}, {'Entry': 'Q15465', 'Length': '462', 'Gene_names': 'SHH', 'PDB ID': '3HO5;3M1N;3MXW;'}]
# above is before adding splits

# [{'Entry': 'O95813', 'Length': '267', 'Gene_names': ['CER1', 'DAND4'], 'PDB ID': ['']}, {'Entry': 'Q8N907', 'Length': '189', 'Gene_names': ['DAND5', 'CER2', 'CKTSF1B3', 'GREM3', 'SP1'], 'PDB ID': ['']}, {'Entry': 'O60565', 'Length': '184', 'Gene_names': ['GREM1', 'CKTSF1B1', 'DAND2', 'DRM', 'PIG2'], 'PDB ID': ['']}, {'Entry': 'P41271', 'Length': '181', 'Gene_names': ['NBL1', 'DAN', 'DAND1'], 'PDB ID': ['4X1J', '']}, {'Entry': 'Q96S42', 'Length': '347', 'Gene_names': ['NODAL'], 'PDB ID': ['4N1D', '']}, {'Entry': 'Q15465', 'Length': '462', 'Gene_names': ['SHH'], 'PDB ID': ['3HO5', '3M1N', '3MXW', '']}]

## 1. Create a function that returns the protein ID of the shortest protein.
def protIDshort():
    sorted_by_length = sorted(newlist4, key=lambda i: i['Length'])
    print ("The protein ID of the shortest protein is", sorted_by_length[0]["Entry"])
protIDshort()
# PROB: will not give more than one of the shortest length(s)


## 2. Create a function that receives a gene name and returns the protein ID. 
gene_name = input("Enter a gene name to get protein ID (or space to exit): ")
while gene_name != "":
    for item in newlist4:
        #if 'DAND4' in item["Gene_names"]:
        for item2 in item["Gene_names"]:
            if gene_name == item2:
                print ("true", item["Entry"])   
    gene_name = input("Enter a gene name to get protein ID (or space to exit): ")
# not getting the correct answer for it becuase its saying that the gene name entered is not defined  
    
## 3. Create a function that receives protein ID and returns the PDB IDs. If the protein doesn’t have PDBs
##    reported, the function should return False. 
proteinID = input("Enter protein ID to recieve PDB ID (or space to exit): ")
while proteinID != "":
    for item in newlist4:
        for item2 in item["Entry"]:
            if proteinID == item2:
                print (item["PDB ID"])
                
                # have to test this separately to be able to do it
    
    
    proteinID = input("Enter protein ID to recieve PDB ID (or space to exit): ")
    