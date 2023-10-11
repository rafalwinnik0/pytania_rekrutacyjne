# x = 10
#
# def f():
#     x = 11
#     print(x)
#
# f() # 11
# print(x) # 10

x = 10

def f():
    global x
    x = 111
    y = 12
    print(x, y)

f()
print(x)