# Write a function that accepts a single integer parameter, and returns True if the number
# is prime, otherwise False.

def prime(a):
    if a>=1 and a//a == 1 and a//1 == a: # get better conditions becuase it returns true for everything
        return True
    else:
        return False
    
    # or can use the code below
def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True