# Write a function that accepts a single integer parameter, and returns a list of the prime
# numbers from 2 to the number.
#--------------------------------------------------------------
#def is_prime(n):
    #for i in range(2, n):
        #if n % i == 0:
            #return False
    #return True

# the above code only shows how to tell if a number is prime or not
# now have to get a way to list all the prime numbers from 2 to the number entered
#---------------------------------------------------------------

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# can use this function and then an if to say that if it is a prime then it will go to the list of primes


#def list_primes(n):
    #numbers = []
    #for i in range(2,n,1):
        #if n % i == 0:
            #return False
        #else:
            #numbers = numbers + [i]
    #return numbers

#print(list_primes(23))

            
# can use the below code but have figure out how this codes really works
#def get_primes(n):
    #numbers = set(range(n, 1, -1)) # becuase have to get all number till 2
    #primes = []
    #while numbers:
        #p = numbers.pop()
        #primes.append(p)
        #numbers.difference_update(set(range(p*2, n+1, p)))
    #return primes