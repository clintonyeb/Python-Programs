def memoize(f):
    cache = {}
    def h(x):
        if x not in cache:
            cache[x] = f(x)
            print('not found in cache')
        return cache[x]
    return h

@memoize
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)
