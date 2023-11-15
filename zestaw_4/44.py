def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

m = 6
print(str(m)+' wyraz cuagu finonacciego', str(fibonacci(n)))