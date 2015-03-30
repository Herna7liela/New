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

## 2. Create a function that receives a gene name and returns the protein ID. 

for item in newlist4:
    #if 'DAND4' in item["Gene_names"]:
    for item2 in item["Gene_names"]:
        if 'DAND4' == item2:
            print ("true", item["Entry"])
        