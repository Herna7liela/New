# A small arts and crafts store owner in the middle of the Karoo has recently upgraded to a
# computerised point of sale system, and wants to do the same for his guest book. Customers
# have previously left their names a small paragraph of comment in the book. The owner would
# like his customers to be able to walk up to a computer near the exit, type in their names,
# and enter a brief comment. He's only interested in a customer's most recent comments, and
# doesn't want store old comments. So repeat customer's must be able to update their previous
# comments. When a repeat customer types in their name, their previous comment is displayed
# back to them, and they are afforded the opportunity to enter a new comment. Should they
# enter a blank line instead of a comment, their previous comment is preserved. Also, if
# instead of a customer name the special command 'quit' is entered, the program exits.
# Similarly the command 'showcomments' causes all customers' names to be displayed, followed
# by their comments slightly indented. Customer's must be able to enter their names in a case
# insensitive manner.

# i want to set up a dictionary that is like comments = [name1,name2 ... etc]      
   
guestbook = {}

name = input("What's your name? (Type 'quit' to exit or 'showcomments' to display guestbook)")   
name = name.lower()

while name != "quit":
    
    if name == "showcomments":
        for name2 in guestbook: # the name2 variable will have the same values as the name key originally had. same concept as the i counter. this is what happens in a for loop
            print (name2,"\n\t", guestbook[name2])
    # if name != "showcomments": 
    else:    
        if name in questbook:
            print ("You already have a comment in the guestbook, here it is: ", guestbook[name])
            comment = input("If you want to keep your old comment then press enter, else for new comment enter new comment: ")
            
            if comment != "":
                guestbook[name] = comment # replaces old comment
            
        else: # elif name!="showcomments":
            comment = input("Enter comment about shop: ")
            guestbook[name] = comment
    
    name = input("What's your name? (Type 'quit' to exit or 'showcomments' to display guestbook)")
    name = name.lower()
    

