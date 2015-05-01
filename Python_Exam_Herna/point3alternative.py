import random
import sys
import os

codon_table = open('codon_table.txt', 'r+')
#codon_table = codon_table.rstrip()
readcodons = codon_table.readlines()
print(readcodons)

i = 0
for i in range(len(readcodons)):
    codons = readcodons[:][i][0:3]
    i += 1
print(codons)

DNA = input("Enter a DNA sequence: ").upper()
#print (DNA)

times = 0
for three in codons:
    if three in range(len(DNA)):
        codons += three
        times += 1
        
codon_dict = {}
codon_dict[codons] = times
print(codon_dict)

# STEPS
# make a file of all the codons
# open file (check)
# strip off the \n
# make a list of all the codons
# enter DNA sequence (check)
# search for codons from list is in sequence entered
# count the amount of that codon in list (check)
# make key for codon
# enter count as the value to the key