# Write a program that asks the user for a list of names ending with a blank line. 
# program then outputs a neat list containing the following, each on their own line,
# labelled: The first name alphabetically. The last name alphabetically, the shortest name,
# and the longest name.

name = input("Type in a name: ")
othername = "ZZZZZ"                               
length = "aaaaaaaaaaaa"
while name != "":
        if name > othername:
                aname = name
        if name < aname:    
                bname = name
        if len(name) < len(length):
                shortname = name
        elif len(name) > len(shortname):
                longname = name
        name = input("Type in a name: ")   # when asking for this name it also has to be inside the loop in order to not just stay in the loop without any repeats
            
print ("First alphabetical name ", aname)
print ("Last aplhabetical name ", bname)
print ("The shortest name is ", shortname)
print ("The longest name is ", longname)
       
 
    