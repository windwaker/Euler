__author__ = 'colmh'

# https://projecteuler.net/archives

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

'''

'''

def is_prime(val):
    if val < 2:
        return False

    if val == 2:
        return True

    for j in range(2, val):
        if 0 == val % j:
            return False

    return True

total = 600851475#143
for i in range(1, total):
    factor = total / i
    #print factor
    if is_prime(factor):
        print factor
        break
