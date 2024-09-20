""" def find_diff(first:int=1, second:int=0)->int:
    return first-second
print(find_diff(20,10))
print(find_diff(second=10,first=20))
print(find_diff(second=10))
print(find_diff())




def change_name(names, index, name):
    names[index] = name
names = ['rahul', 'modi']
print(names)
change_name(names,1,'modiji')
print(names)


print(sum([0,20,30])) """ #iterable object..



# type([10,20,30]).__iter__


""" def find_sum(first, second, *others):
    s = first + second
    if(len(others)>0):
        for num in others:
            s += num

    return s
print(find_sum(10,20))
print(find_sum(10,20,30))
print(find_sum(10,20,30,40,50)) """




""" def find_sum(first, second, **others):
    s = first + second
    if(len(others) > 0):
        for key in others:
            s += others[key]
    return s
print(find_sum(first=10, second=20))
print(find_sum(first=10, second=20, third=30))
print(find_sum(first=10, second=20, third=30, fourth=40)) """




""" def fact(N):
    if N <= 1: # base/edge case
        return 1
    
    return N * fact(N - 1)
print(fact(5)) """


import math
def isPrime(N):
    N_sqrt = int(math.sqrt(N))
    for i in range(2,N_sqrt+1):
        if N % i == 0:
            return False
        
    return True
print(isPrime(5))
print(isPrime(51))
print(isPrime(65))