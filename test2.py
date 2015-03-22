alphabet= 'abcdefghijklmnopqrstuvwxyz'
alphabetCount = 0
s=(input('enter a string')).lower()
    
if len(s) < 26:
   print("Phrase not long enough")
   
else:
   for i in range(len(alphabet)):
      if alphabet[i] in s:
         alphabetCount = alphabetCount + 1
   if alphabetCount == 26:
      print("True")
   else:
      print("False")