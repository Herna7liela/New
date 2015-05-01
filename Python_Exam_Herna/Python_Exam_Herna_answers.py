# Question 1
import random
import sys
import os

# to input a dna sequence
DNAseq = str(input("Enter a dna sequence: "))
DNAseq = DNAseq.upper()

# display the weight of each base
def cumulative_weight(DNAseq):
    while DNAseq != "":
        cumweight = 0
        for i_base in range(len(DNAseq)):
            if DNAseq[i_base] == "A":
                base = "A"
                weight = 313.21
                cumweight += weight
            if DNAseq[i_base] == "T":
                base = "T"
                weight = 304.20
                cumweight += weight
            if DNAseq[i_base] == "C":
                base = "C"
                weight = 289.18
                cumweight += weight 
            if DNAseq[i_base] == "G":
                base = "G"
                weight = 329.21
                cumweight += weight  
            ##else:
                #print("Enter a sequence with A,T,G,C and not other characters.")
            print(base, "\t", weight, "\t", cumweight, "\n")
        break
    else:
        print("No sequence was enter, reinitiate the program and enter a DNA sequence.")
            
            
# call cumulative weight function
cumulative_weight(DNAseq)
## the format is not completely right on this one

# formatting of file    
print("\n")    
print("----------------------")

# to calculate the weight contributed per base
def weight_contrib_base(DNAseq):
    countG = 0
    countA = 0
    countT = 0
    countC = 0
    weight_A = 313.21
    weight_T = 304.20 
    weight_C = 289.18
    weight_G = 329.21
    for count in range(len(DNAseq)):
        if DNAseq[count] == "G":
            countG = countG+1
        if DNAseq[count] == "A":
            countA = countA+1
        if DNAseq[count] == "T":
            countT = countT+1
        if DNAseq[count] == "C":
            countC = countC+1
    
        contribA = countA*(weight_A)
        contribT = countT*(weight_T)
        contribC = countC*(weight_C)
        contribG = countG*(weight_G)
    
    print("Weight contribution per base:")
    print("A = ", contribA)
    print("C = ", contribC)
    print("G = ", contribG)
    print("T = ", contribT)

# call function
weight_contrib_base(DNAseq)

print("\n")

# print the total weight
## I used most of the code of cumulative_weight()
def total_weight(DNAseq):
    while DNAseq != "":
        total_weight = 0
        for i_base in range(len(DNAseq)):
            if DNAseq[i_base] == "A":
                base = "A"
                weight = 313.21
                total_weight += weight
            if DNAseq[i_base] == "T":
                base = "T"
                weight = 304.20
                total_weight += weight
            if DNAseq[i_base] == "C":
                base = "C"
                weight = 289.18
                total_weight += weight 
            if DNAseq[i_base] == "G":
                base = "G"
                weight = 329.21
                total_weight += weight  
        print("Total weight: ", total_weight)
        break
    else:
        return

# call the total weight function    
total_weight(DNAseq)

--------------------------------------------------------------------------------------------------------------
# Question 2
import random
import sys
import os

#a = input("enter tuple a: ")
#b = input("enter tuple b: ")
#a = tuple(a)
#b = tuple(b)
## did this just to see if it works

# possibly have to make this a module so it can be used in the shell

def add(a,b):
    add = a + b
    print(add)
    return 


def subtract(a,b):
    subtract = a - b
    print(subtract)
    return 
    

def dot(a,b):
    prod_0 = a[0]*b[0]
    prod_1 = a[1]*b[1]
    prod_2 = a[2]*b[2]
    dot = prod_0 + prod_1 + prod_2
    print(dot)
    return 
    
    
def cross(a,b):
    if a == b*c:
        a = [ax,ay,az]
        b = [bx,by,bz]
        c = [ca,cy,cz]
        ax = by*cz - bz*cy
        ay = bz*cx - bx*cz
        az = bx*cy - by*cx  
    print(cross)
    return
    
----------------------------------------------------------------------------------------------------------
# Question 3 (first try) = please also look at second try
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

----------------------------------------------------------------------------------------------------------
# Question 3 second try
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

---------------------------------------------------------------------------------------------------------
# Question 4
import random
import sys
import os

reads_file = open('reads.txt', 'r+')
read_readsfile = reads_file.readlines()

#print(read_readsfile)



print("POS \t | \t 1 2 3 4 5 6 7 8 \t | Consensus \n ------------------------------------------------------")

for pos in range(1,26):
    print (pos)
  
for line in read_readsfile:
    if line.startswith("1"):
        dna1 = line.split()
        
DNA = read_readsfile.split("\n") 
print(DNA)
#for base in range(stop):

-------------------------------------------------------------------------------------------------------------
