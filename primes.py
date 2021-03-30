import numpy as np

def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        k = 2
        while k*k <= n:
            if n % k == 0:
                return False
            k += 1
        return True
        
        

def isPrimeList(num):
    L = []
    for n in num:
        L.append((n,isPrime(n)))
    return L


def allPrimesList(n):
    L = []
    for m in range(2,n+1):
        if(isPrime(m)):
            L.append(m)
    return np.array(L)



def isPrimeSubSet(num):
    num.sort()
    L = []
    for n in num:
        if(isPrime(n)):
            L.append(n)
    return np.array(num)


def PrimeFactors(n):
    primes = allPrimesList(int(np.sqrt(n)))
    p_factors = []
    for prime in primes:
        if n%prime == 0:
            p_factors.append(prime)
            if isPrime(int(n/prime)):
                p_factors.append(int(n/prime))
    return np.array(p_factors)        

def factorise(n):
    prime_factors = PrimeFactors(n)
    fctsd_AuxList = []
    for factor in prime_factors:
        count = 0
        while(n%factor == 0):
            count += 1
            n = int(n/factor)
        fctsd_AuxList.append((factor,count))
    return np.mat(fctsd_AuxList)


print(factorise(12344))
