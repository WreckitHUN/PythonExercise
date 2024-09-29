# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

def fib(num: int):
    a = 0
    b = 1
    for i in range(num):
        yield a
        c = a
        a = b
        b = c + b


for i in fib(1):
    print(i)
