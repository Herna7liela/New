import random
import sys
import os

#a = input("enter tuple a: ")
#b = input("enter tuple b: ")
#a = tuple(a)
#b = tuple(b)
## did this just to see if it works

# possibly have to make this a module so it can be used in the shell

def add(a,b):
    add = a + b
    print(add)
    return 


def subtract(a,b):
    subtract = a - b
    print(subtract)
    return 
    

def dot(a,b):
    prod_0 = a[0]*b[0]
    prod_1 = a[1]*b[1]
    prod_2 = a[2]*b[2]
    dot = prod_0 + prod_1 + prod_2
    print(dot)
    return 
    
    
def cross(a,b):
    if a == b*c:
        a = [ax,ay,az]
        b = [bx,by,bz]
        c = [ca,cy,cz]
        ax = by*cz - bz*cy
        ay = bz*cx - bx*cz
        az = bx*cy - by*cx  
    print(cross)
    return
    
    
    