import math
def applyToEach(L, f):
    """Assumes L is a list, f a function
    Mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)

L = [1, -2, 3.33]
print('L =', L)
applyToEach(L, abs)
print('L =', L)
applyToEach(L, int)
print('L =', L)
applyToEach(L,math.factorial)
print('L =', L)
applyToEach(L, fib)
print('L =', L)
