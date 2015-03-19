nucleotide = input("Enter a nucleotide sequence")
counter = 0
lowernucleotide = ""
while counter <= len(nucleotide):
    if nucleotide[counter] =='A':
        lowernucleotide = lowernucleotide + 'a'
    if nucleotide[counter] == 'T':
        lowernucleotide = lowernucleotide + 't'
    if nucleotide[counter] == 'G':
        lowernucleotide = lowernucleotide + 'g'
    if nucleotide[counter] == 'C':
        lowernucleotide = lowernucleotide + 'c'
    counter = counter + 1
    
    print (lowernucleotide)
    
    # have add in a step to be able to not concatenate the seq is mixed characters are used
    