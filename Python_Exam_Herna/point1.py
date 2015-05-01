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