__author__ = 'wangchen'
class InvalidInputError(Exception)


# recursive implementation
def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

# iterative implementation
def fib2(n):
    prev = 0
    curr = 1
    for i in range(1, n+1):
        tmp = prev
        prev = curr
        curr = tmp + curr
    return prev

# iterative implementation with arrays
def fib3(n):
    l = [0, 1]
    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])
    return l[n]

fib1(25)
fib2(25)
fib3(25)