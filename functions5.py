# Write a function that accepts a single integer parameter, and returns a list of the prime
# numbers from 2 to the number.

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

# the above code only shows how to tell if a number is prime or not
# now have to get a way to list all the prime numbers from 2 to the number entered

def list_primes(n):
    for i in range(2,n):
        numbers = [""]
        if n % i != 0:
            numbers += i
    return numbers

# still have to test this code to see if it is functional and gives a list of prime numbers
# in the correct range(2,n)
            
# can use the below code but have figure out how this codes really works
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes