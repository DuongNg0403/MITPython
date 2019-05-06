#The short but inefficient way
'''
def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(120))
'''
#The a little bit longer and efficient way

def fib(n,store):
    if n in store:
        return store[n]
    else:
        ans = fib(n-1,store)+fib(n-2,store)
        store[n]= ans
        return ans

store = {1:1,2:2}
print(fib(4,store))
