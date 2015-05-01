import random
import sys
import os

reads_file = open('reads.txt', 'r+')
read_readsfile = reads_file.readlines()

#print(read_readsfile)



print("POS \t | \t 1 2 3 4 5 6 7 8 \t | Consensus \n ------------------------------------------------------")

for pos in range(1,26):
    print (pos)
  
DNA = read_readsfile.split("\n") 
print(DNA)
#for base in range(stop):