text = """
Entry	Gene names	Cross-reference (PDB)	Length
O95813	CER1 DAND4		267
Q8N907	DAND5 CER2 CKTSF1B3 GREM3 SP1		189
O60565	GREM1 CKTSF1B1 DAND2 DRM PIG2		184
P41271	NBL1 DAN DAND1	4X1J;	181
Q96S42	NODAL	4N1D;	347
Q15465	SHH	3HO5;3M1N;3MXW;	462"""
#print (text)

split_text = (text.split("\n"))
char_list = []
charlist = ""

for char in split_text:
    morpho = {}
    if char != "\t":
        charlist = charlist + char
    else:
        char_list = char_list + [charlist]
        charlist = ""
    if charlist != "":
        char_list = char_list + [charlist]
    morpho["Entry ID"] = char_list
    
print (morpho["Entry ID"])
    ###########
    
    # maybe can split these things according to the char one in movies and then moving char by char to find a 
    #"\t" or "\t\t" and ";" split it into another key:value pair
