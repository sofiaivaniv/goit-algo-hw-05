from collections.abc import Callable

def caching_fibonacci() -> Callable[[int], int]:
    '''Returns a Fibonacci function with caching.'''
    cache = {}
    def fibonacci(n: int) -> int:
        '''Computes the nth Fibonacci number recursively with caching.'''
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()

print(fib(10)) 
print(fib(15)) 