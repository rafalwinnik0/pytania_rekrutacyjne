# 1 moje
# def rekurencja(n):
#     x = 0
#     y = 1
#     print(x)
#     print(y)
#     for i in range(2, n+1):
#         print(x+y)
#         x1 = x
#         x = y
#         y = x1 + y
#
# rekurencja(10)

# 2
# def fibonacci_n(n):
#     if n <= 1:
#         return n
#     return fibonacci_n(n - 1) + fibonacci_n(n - 2)
#
# print(fibonacci_n(10))

# 3
def fibonacci(n):
    p, d = 0, 1
    for i in range(n):
        print(f"i: {i}")
        print(f"p: {p}, d: {d}")

        p, d = d, p + d

        print(f"p: {p}, d: {d}")
        print(p)
    return p

print(fibonacci(10))


