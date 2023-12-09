def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

n = 10
fib_number = fibonacci_number(n)
print(fib_number)
