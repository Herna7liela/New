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

question = input("Do you want to enter a comment? (Y/N): ") # must change this so can enter name

while question == "Y":
    comments = {}
    comments["name"] = input("Enter customer name: ")
    name = name.lower()
    comments["comment"] = input("Enter comment about shop: ")
    if name in comments: # i want to say that if there exists a specific name in dict then just add to the comment or replace it with newer one, but maybe this should be higher up in code
        comment = ''
        comment = comment + "comment"
    elif name not in comments:
        comments = {}
        comments["name"] = input("Enter customer name: ")
        name = name.lower()
        comments["comment"] = input("Enter comment about shop: ")        
    
    # must get something when a blank comment is added that the previous comment is then kept
## all questions answers must be entered case insensitively. maybe can store everything as lower case  
## set up dictionary to contain different parts called names that then contain comments
## must maybe ask for name first to see if name is already stored in memory
## if name is there then display previous comment and just replace previous comment
    ##with new comment about shop
## if they then enter a blank line then previous comment is preserved
## else if name is not there then can ask for name and comment
## ask a question to enter quit after which the program is ended
## if command showcomments is entered then all the names and comments on printed on the screen