herna@herna-X550LC:~$ python3
Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print "Hello world"
  File "<stdin>", line 1
    print "Hello world"
                      ^
SyntaxError: invalid syntax
>>> print (Hello world)
  File "<stdin>", line 1
    print (Hello world)
                     ^
SyntaxError: invalid syntax
>>> print ('Hello world')
Hello world
>>> print (1)
1
>>> print (173+92)
265
>>> print (173+92.0)
265.0
>>> print (Hello)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> print ("Jane has",7,"apples")
Jane has 7 apples
>>> print ("Jane has " "7 " "apples")
Jane has 7 apples
>>> print ("Jane has " "7 " "apples","*")
Jane has 7 apples *
>>> print ("Jane has " "7 " "apples",end="*")
Jane has 7 apples*>>> 
>>> print 1
  File "<stdin>", line 1
    print 1
          ^
SyntaxError: invalid syntax
>>> print "hello"
  File "<stdin>", line 1
    print "hello"
                ^
SyntaxError: invalid syntax
>>> print ("hello")
hello
>>> print ("Herna")
Herna
>>> print ("de Wit")
de Wit
>>> print ("Herna " "de Wit)
  File "<stdin>", line 1
    print ("Herna " "de Wit)
                           ^
SyntaxError: EOL while scanning string literal
>>> print ("Herna","de Wit")
Herna de Wit
>>> firstname = Herna
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Herna' is not defined
>>> firstname = "Herna"
>>> surname = "de Wit"
>>> print = firstname,surname
>>> print = (firstname,surname)
>>> end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'end' is not defined
>>> firstname
'Herna'
>>> surname
'de Wit'
>>> print 'firstname','surname'
  File "<stdin>", line 1
    print 'firstname','surname'
                    ^
SyntaxError: invalid syntax
>>> print (firstname,surname)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> print (firstname surname)
  File "<stdin>", line 1
    print (firstname surname)
                           ^
SyntaxError: invalid syntax
>>> print (firstname surname )
  File "<stdin>", line 1
    print (firstname surname )
                           ^
SyntaxError: invalid syntax
>>> "Hello"
'Hello'
>>> MUCH madness is divinest sense,"
  File "<stdin>", line 1
    MUCH madness is divinest sense,"
               ^
SyntaxError: invalid syntax
>>> print "To a discerning eye;"
  File "<stdin>", line 1
    print "To a discerning eye;"
                               ^
SyntaxError: invalid syntax
>>> print "Much sense the starkest madness."
  File "<stdin>", line 1
    print "Much sense the starkest madness."
                                           ^
SyntaxError: invalid syntax
>>> print "'T is the majority", "In this, as all, prevails."
  File "<stdin>", line 1
    print "'T is the majority", "In this, as all, prevails."
                             ^
SyntaxError: invalid syntax
>>> print "Assent, and you are sane;"
  File "<stdin>", line 1
    print "Assent, and you are sane;"
                                    ^
SyntaxError: invalid syntax
>>> print ("""Demur,-you're straightway dangerous,
... in this, as all, prevails,
... assent, and you are sane.""")
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: 'tuple' object is not callable
>>> assent, and you are sane""")
  File "<stdin>", line 1
    assent, and you are sane""")
              ^
SyntaxError: invalid syntax
>>> print ("""Demur,-you're straightway dangerous,
... hdsbjfb
... nkasndkas""")
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: 'tuple' object is not callable
>>> print """ ksndksn
... skdksnds
... skdskdj"""
  File "<stdin>", line 3
    skdskdj"""
             ^
SyntaxError: invalid syntax
>>> print """ jskdnksjd
... skdksa """
  File "<stdin>", line 2
    skdksa """
             ^
SyntaxError: invalid syntax
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> x = 2
>>> x
2
>>> y = 3
>>> z = 5
>>> print ("x,y,z")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> print x y z
  File "<stdin>", line 1
    print x y z
          ^
SyntaxError: invalid syntax
>>> print x, y, z
  File "<stdin>", line 1
    print x, y, z
          ^
SyntaxError: invalid syntax
>>> print (x,y,z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> name = "My name is James"
>>> age = "I am 30 years old"
>>> height = "1.78 meters tall"
>>> print (name,age,"and",height)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> print ('name,age,"and",height')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> print name,age,"and",height
  File "<stdin>", line 1
    print name,age,"and",height
             ^
SyntaxError: invalid syntax
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> 
KeyboardInterrupt
>>> name = "Herna"
>>> age = "23"
>>> height = "1.58"
>>> print ("my name is %s, I am %s years old and %s meters short " % (name,  ge, 
... print ("my name is %s, I am %s years old and %s meters short " % (name,  ge, 
... 
KeyboardInterrupt
... 
... 
KeyboardInterrupt
... 
KeyboardInterrupt
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> name = "Herna"
>>> age = "23"
>>> height = "1.58"
>>> print ("I am", name, "and", age, "years old")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> print ('"I am", name, "and", age, "years old"')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
herna@herna-X550LC:~$ python3
Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> name = "Herna"
>>> age = "23"
>>> height = "1.58"
>>> print ('"I am", name, "and", age, "years old"')
"I am", name, "and", age, "years old"
>>> print ("I am", name, "and", age, "years old")
I am Herna and 23 years old
>>> exit()
herna@herna-X550LC:~$ python3
Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print ("the cat\'s mat")
the cat's mat
>>> print ('the cat\'s mat')
the cat's mat
>>> print ("the cat's mat")
the cat's mat
>>> print ("""shdnwodbs...
... kadaskasdhs
... jaksdkasdks""")
shdnwodbs...
kadaskasdhs
jaksdkasdks
>>> print "Jane has", 7, "apples"
  File "<stdin>", line 1
    print "Jane has", 7, "apples"
                   ^
SyntaxError: invalid syntax
>>> print ("Jane has", 7, "apples")
Jane has 7 apples
>>> touch Exercises4.py
  File "<stdin>", line 1
    touch Exercises4.py
                   ^
SyntaxError: invalid syntax
>>> touch Exercises.py
  File "<stdin>", line 1
    touch Exercises.py
                  ^
SyntaxError: invalid syntax
>>> gedit exercises.py
  File "<stdin>", line 1
    gedit exercises.py
                  ^
SyntaxError: invalid syntax
>>> vim exercises.py
  File "<stdin>", line 1
    vim exercises.py
                ^
SyntaxError: invalid syntax
>>> git status
  File "<stdin>", line 1
    git status
             ^
SyntaxError: invalid syntax
>>> end ()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'end' is not defined
>>> exit()
herna@herna-X550LC:~$ python3
Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> gedit exercises.py
  File "<stdin>", line 1
    gedit exercises.py
                  ^
SyntaxError: invalid syntax
>>> touch exercises.py
  File "<stdin>", line 1
    touch exercises.py
                  ^
SyntaxError: invalid syntax
>>> vim exercises.py
  File "<stdin>", line 1
    vim exercises.py
                ^
SyntaxError: invalid syntax
>>> exit()
herna@herna-X550LC:~$ python3
Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> git status
  File "<stdin>", line 1
    git status
             ^
SyntaxError: invalid syntax
>>> exit()


herna@herna-X550LC:~$ python3
Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> name = "James"
>>> print (name)
James
>>> i = 1
>>> j = i
>>> i = 2
>>> print ("i =", i, "and j=", j) 
i = 2 and j= 1
>>> x = x+1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> x = 3+6
>>> x
9
>>> x = 7
>>> x = x+1
>>> x
8
>>> x = 21
>>> x = x+1
>>> print (x)
22
>>> 5/2
2.5
>>> 5//2
2
>>> 5%2
1
>>> 2%2
0
>>> 20%2
0
>>> 2745336%2
0
>>> 2745337%2
1
>>> print ("5 divided by 2 is", 5/2, "but also", 5//2, "and the amount left over is", 5%2)
5 divided by 2 is 2.5 but also 2 and the amount left over is 1
>>> "some"+"thing"
'something'
>>> "ha"*7
'hahahahahahaha'
>>> "ha"*5/2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> "ha"*5
'hahahahaha'
>>> "something"[5]
'h'
>>> "something"
'something'
>>> print (x[5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> print [5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> "something" [5]
'h'
>>> x = "something"
>>> print (x[2:4])
me
>>> print (x[5: ])
hing
>>> print (x[-3])
i
>>> print (x[-5])
t
>>> i = 7
>>> i/4
1.75
>>> i%4
3
>>> "x"*1000
'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
>>> s = "Harry's Hippie Hoedown"
>>> s + ": tickets only $5"
"Harry's Hippie Hoedown: tickets only $5"
>>> s + ": tickets only" + "5"*3
"Harry's Hippie Hoedown: tickets only555"
>>> s + ": tickets only $" + "5"*3
"Harry's Hippie Hoedown: tickets only $555"
>>> "ABBA was a Swedish band popular during the 80's"[0:4]
'ABBA'
>>> "ABBA was a Swedish band popular during the 80's"[-15:-7]
'during t'
>>> s = "ABBA was a Swedish band popular during the 80's"
>>> "BAAB"+s[4:11]+"Danish"+s[18:24]+"un"+s[24:-4]+"90's"
"BAAB was a Danish band unpopular during the 90's"
>>> 


