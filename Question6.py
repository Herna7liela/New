# Write a program that takes a DNA sequence and returns the number of non-nucleotide bases.

# suppose 'n' is the non-nucleotide bases

dna = input("Enter a DNA sequence: ")

while dna != "":
    dnalow = dna.lower()
    count = 0
      
    for nonnucleotide in dnalow:
        if nonnucleotide == 'n' in dnalow:
            count = count + 1
        else:
            continue
    print (count)
    dna = input("Enter a DNA sequence: ")  

