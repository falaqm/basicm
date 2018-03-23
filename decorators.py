import time

''' wrap function in another function-fns are first class objects
    you can pass and return as any other variable'''
def timez(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,*kwargs)
        end=time.time()
        print(func.__name__+" took "+str((end-start)*1000)+" mili sec")
    return wrapper

@timez
def calsqr(num):
    result=[]
    for n in num:
        result.append(n*n)
    return result

@timez
def calcube(num):
    result = []
    for n in num:
        result.append(n * n * n)
    return result

array=range(1,10000)
outsquare=calsqr(array)
outcube=calcube(array)

print('baby')
