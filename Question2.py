# A pangram is a sentence that contains all the letters of the English alphabet at least
# once, for example: The quick brown fox jumps over the lazy dog. Your task here is to
# write a function to check a sentence to see if it is a pangram or not.



possible = input("Enter a sentece to check if its a pangram: ")

while possible != "":
    possible = possible.lower()
    if possible == set('abcdefghijklmnopqrstuvwxyz'):
        print ("True")
    else:
        print ("False")
        
    possible = input("Enter a sentece to check if its a pangram: ")
    
    # so this code keeps giving a "False" output with whatever I put in. 
    # also if I don't use the set() I don't know what else to use