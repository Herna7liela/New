possible = input("Input a sentence: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'

while possible != 0:
    possible = possible.lower()
    if [i] in possible(0,26,1) == alphabet:
        print ("True")
    else:
        print ("False")
    