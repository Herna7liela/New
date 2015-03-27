# Extend your solution to the previous problem, by allowing customers to enter multi-line
# comments, and to terminate their comments by entering a blank line. If the comment is
# entirely blank, i.e. the first line is blank, then it does not overwrite the former comment
# if any. Also, ensure that when the comments are outputted back, either because of the
# 'showcomments' command, or a repeat customer entering their name, that the line width of
# the outputted comments does not exceed 60 characters, nor break a word in two, i.e. lines
# are only broken on white space.

# capturing multi lines
def capture_multiline_comment():
    multiline = ""
    comment = input("Enter comment about shop: ")
    while comment != "":
        multiline += comment + " "#+ "\n"
        comment = input(": ")
    return multiline

def print_lines60(text):
    rest = text[:] 
    while len(rest)>60:
        pos = rest[0:60].rfind(" ") # instead of +1 below can add a +1 at the end of this line
        print ("\t"+rest[0:pos+1])
        rest = rest[pos+1:]
    print ("\t"+rest)

guestbook = {}

name = input("What's your name? (Type 'quit' to exit or 'showcomments' to display guestbook)")   
name = name.lower()

while name != "quit":
    
    if name == "showcomments":
        for name2 in guestbook: 
            print (name2,"\n\t")
            print_lines60(guestbook[key])
    
    else:    
        if name in questbook:
            print ("You already have a comment in the guestbook, here it is: ")
            print_lines60(guestbook[key])
            
            if comment != "":
                guestbook[name] = comment 
            
        else: 
            comment = capture_multiline_comment()
            guestbook[name] = comment
    
    name = input("What's your name? (Type 'quit' to exit or 'showcomments' to display guestbook)")
    name = name.lower()
    
    
# capturing multi lines
#def capture_multiline_comment():
    #multiline = ""
    #comment = input("Enter comment about shop: ")
    #while comment != "":
        #multiline += comment #+ "\n"
        #comment = input(": ")
        #return multiline
    
#print (multiline)


# now to create a program that only accepts 60 characters
#text = "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbccccccccccccccccccccdddddddddddddddddddddddddddeeeeeeeeeeeee"
#x = ""
#if len(text)> 60:
    #for i in range(0, len(text), 60):
        #x = text[i:i+60]
        #print (x)
# the above code only slices things at len = 60 but this doesnt help because it cuts words
 ##### i dont know what to do now!!!!!!!!!!1
#def print_lines60(text):
    #rest = text[:] 
    #while len(rest)>60:
        #pos = rest[0:60].rfind(" ") # instead of +1 below can add a +1 at the end of this line
        #print (rest[0:pos+1])
        #rest = rest[pos+1:]
    #print (rest)