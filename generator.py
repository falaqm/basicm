# '''generator---simple way of generating iterator'''
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#
# for f in fib():
#     if f>100:
#         break
#     print(f)

'''Fibonnaci using generators'''


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for c in fib():
    if c > 13:
        break
    print(c)
