import random
import sys
import os

DNA = input("Enter a DNA sequence: ").upper()
#print (DNA)

codon_table = open('codon_table.txt', 'r+')
readcodons = codon_table.readlines().strip()

codonstry_dict = {} # just created to see differences in output between two dictionaries
codons_dict = {}
#def codon_count(DNA):
for codon in readcodons:
    if codon != "":
        codon_info = readcodons.rstrip()
        codonstry_dict["CODONTRY"] = codon_info
        codons_dict["CODON"] = readcodons # now have one huge key!!!
    #return
print (codons_dict)
print(codonstry_dict)

count = 0
c = len(DNA)
possible_codons = []
for c in codons_dict:
    if c in DNA:
        print(c)
        count +=1
codons_dict["CODON"] = count

# to sort the values
values = sort(codons_dict.values())
sorted_times = codons_dict[:][1].sort()
    
print("CODON  TIMES\n")
print(c,count)