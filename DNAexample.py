
dna = "atttgatctagatTTTTTgatagctagaCCaTGAcccccccatagatacatg"
copydna = ""
# creating an uppercase copy of dna
for i in range(len(dna)):            # short way is to say print(dna.upper())
    if dna[i]=="a":
        copydna = copydna + "A"
    elif dna[i]=="t":
        copydna = copydna + "T"
    elif dna[i]=="g":
        copydna = copydna + "G"
    elif dna[i]=="c":
        copydna = copydna + "C"
    else:
        copydna = copydna + dna[i]
    
print (dna)
print (copydna)

# reverse by using negative indexes
reverse = ""
for i in range(1,len(dna)+1):         # can also give arguments for the range and add to end point +/-1
    reverse = reverse + copydna[-i] # looking at position -1 becuase then you start at the end
    
reverse2 = ""
for i in range(1,len(copydna)):
    reverse2 = copydna[i] + reverse2
    # if adding print here, then it shows how string is made
print (reverse)
print (reverse2)
print (reverse==reverse2)
print (reverse[10:]) # seq is printed from 10 to the end
print (reverse[10:20:-1]) # also doing the reverse

# now have to change string into rna
rna = ""
for i in range(len(reverse)):
    if reverse[i] == "T":
        rna = rna + "U"
    else:
        rna = rna + reverse[i]
    
    
print (rna)
    