# Write a program the reads strings until a blank line is encountered. For each string
# entered, treat the portion of the string up to the first colon (or the entire string
# if no colon is present) as a key name, and everything after the first colon as a value.
# If the key portion has been entered before, print out the old value paired with that key,
# and then change the value to the newly entered one. After the blank line, print out a neat
# list of key value pairs.

stringa = input("Enter a string: ")
stringb = input("with two parts:  ")
stringc = ''
print (stringa, stringb)

while stringa !='':
    if stringc == (stringa,stringb):
        print (stringc)
    stringb = input("Enter stringb: ")    
    while stringb !='':
            if stringc == (stringa, stringb):
                print (stringc)
            stringa = input("Enter stringa: ")    # i need to get back into previous loop
    print ("The key value pairs are: ", stringa, stringb)  
    
# staying stuck in the last while loop and need to get out to go to upper one
# also still have to make a list of all the key value pairs
# can possible make a list by adding all the printed pairs to a dictionary
# can then just print the dictionary at the end

#enter the key string
# enter the value string
# add them together in a tuple

