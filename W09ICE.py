from sympy import primerange

def getPrimeGaps():
    list_of_gaps = []
    prev = 3
    gap = 0
    for prime in list(primerange(4, 10000001)):
        gap = prime - prev
        prev = prime
        list_of_gaps.append(gap)
    return list_of_gaps

def restorePrimes(list_of_gaps):
    list_of_primes = [2, 3]
    for gap in list_of_gaps:
        list_of_primes.append(list_of_primes[-1] + gap)
    return list_of_primes

print(restorePrimes(getPrimeGaps())[:100])