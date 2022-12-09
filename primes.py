"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if(number_of_primes<=0):
        raise ValueError("Only integers greater than 0 are allowed")
 
    numberToCheck = 2

    while number_of_primes:
        if isPrime(numberToCheck):
            list.append(numberToCheck)
            number_of_primes = number_of_primes-1
        numberToCheck = numberToCheck+1
    
    return list

def isPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if(numberToCheck%x == 0):
            return False
    return True









