possible = input("Enter a sentece to check if its a pangram: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 0
while possible != "":
    possible = possible.lower()
    
    if len(possible) < 26:
        print ("Not enough letters.")
    else:
        if possible == set('abcdefghijklmnopqrstuvwxyz'):
            print ("True")
        else:
            print ("False")
        
    possible = input("Enter a sentece to check if its a pangram: ")
    
   