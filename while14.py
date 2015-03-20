# Write a program that asks the user to enter two different phrases, and a single letter.
# Count the number of occurrences of the inputed letter in each phrase and output the
# phrase with the most occurrences.

phrase1 = input("Enter first phrase: ")
phrase2 = input("Enter second phrase: ")
letter = input ("Enter a single letter: ")

while phrase1 != "":
    phrase1oc = phrase1.count(letter)
    phrase2oc = phrase2.count(letter)
    print ("The occurrences of ", letter, "in phrase1 is: ", phrase1oc)
    print ("The occurrences of ", letter, "in phrase2 is: ", phrase2oc)    
    if phrase1oc > phrase2oc:
        print ("phrase1 has the most occurrences of ", letter)
    if phrase2oc > phrase1oc:
        print ("phrase2 has the most occurences of ", letter)
    elif phrase1oc == phrase2oc:
        print ("both phrases have equal occurrences of ", letter)
    phrase1 = input("Enter first phrase: ")
    phrase2 = input("Enter second phrase: ")
    letter = input ("Enter a single letter: ")    

   