#3.Write a program that starts by declaring the above dictionary as a literal, and outputs
# the books in order.

books = {1: "Hitchhiker's Guide to the Galaxy", 2: "The Restaurant at the End of the Universe", 3: "Life, the Universe, and Everything", 4: "So Long, and Thanks for all the Fish!", 5: "Mostly Harmless"}    

books = books.items()
lastbook = ("999999, Zzzzzzz")

for book in books:
    if lastbook > book[1]:
        lastbook = book
print (lastbook)