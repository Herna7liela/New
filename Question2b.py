
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


