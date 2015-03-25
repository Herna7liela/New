#4.Write a program that starts by declaring the above dictionary as a literal, and then
# asks the user for a number, and prints out name of the book which has the given number.

books = {1: "Hitchhiker's Guide to the Galaxy", 2: "The Restaurant at the End of the Universe", 3: "Life, the Universe, and Everything", 4: "So Long, and Thanks for all the Fish!", 5: "Mostly Harmless"}    

books = books.items()

key = int(input("Enter a number: "))

for book in books:
    if k in range(key):
        print (books[key])
