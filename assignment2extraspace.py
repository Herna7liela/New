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

## 5. Create a function that prints a list of pairs of all the reported combinations of genes and PDBs

# def combo_gene_pdb():
counter1 = 0
counter2 = 0
for item in newlist4:
    #print (item)
    for item2 in item["Gene_names"]:
        #print (item["Gene_names"])
        for item3 in item["PDB ID"]:
            #print (item["Gene_names"], ":", item["PDB ID"])
            # can now use counter to change the index to print each combination
            counter1 = counter1 + 1
            counter2 = counter2 + 1
            print (item["Gene_names"][counter1], ":", item["PDB ID"][counter2])






# combo_gene_pdb()
    
        