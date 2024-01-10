def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 + fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
