def isOdd(N):
    return N % 2 == 1
def isEven(N):
    return N % 2 == 0
import math
def isPrime(N):
    N_sqrt = int(math.sqrt(N))
    for i in range(2,N_sqrt+1):
        if N % i == 0:
            return False
        
    return True

    