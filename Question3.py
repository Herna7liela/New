# Write a program that ask the user to input a text and then recognises palindromes
#(i.e. words that look the same written backwards). For example, "radar" is a palindrome.


word = input("Enter a word to test for palindrome: ")

while word != "":
    word1 = word.lower()
    if word1 == word1[::-1]:
        print ("True")
    elif word1 != word1[::-1]:
        print ("False")
    
    word = input("Enter a word to test for palindrome: ")
