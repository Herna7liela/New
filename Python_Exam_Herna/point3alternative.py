import random
import sys
import os

DNA = input("Enter a DNA sequence: ").upper()
#print (DNA)

codon_table = open('codon_table.txt', 'r+')
readcodons = codon_table.readlines().strip()