def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def do_nothing():
    x = 5 + 7
    return x

def add(x,y):
    return x + y
