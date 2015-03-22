# A pangram is a sentence that contains all the letters of the English alphabet at least
# once, for example: The quick brown fox jumps over the lazy dog. Your task here is to
# write a function to check a sentence to see if it is a pangram or not.

string = input("Enter a sentence: ")
string = string.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
empty = ""
for i in string:
    if i in alphabet:
        empty = empty + i
strlen = len(empty)
if strlen == len(alphabet):
    print ("Sentence is a pangram")
else:
    print ("Sentence is not a pangram")

