# Write a function that accepts a single integer parameter, and returns a list of the prime
# factors of that number.

# use the previous exercise's code and just add to it to only add the factors
def list_primes(n):
    for i in range(2,n):
        numbers = [""]
        if n % i != 0:
            numbers += i
    return numbers
# with this I so far only get a list of the prime numbers within the range(2,n)
# now need to get the factors of the prime numbers in the range of primes

