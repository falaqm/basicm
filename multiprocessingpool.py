# from multiprocessing import Pool
# import time
# def f(n):
#     sum =0
#     for x in range(10000):
#         sum+= x*x
#     return sum
# if __name__=='__main__':
#     t1=time.time()
#     #array=[1,2,3,4,5]
#     p=Pool(processes=15)
#     result=p.map(f,range(10000))
#     p.close()
#     p.join()
#     print("Pool took",time.time()-t1)
#     result=[]
#     t2=time.time()
#     for x in range(10000):
#         result.append(f(x))
#     print('serial processing took',time.time()-t2)


# Simple pgm
from multiprocessing import Pool
import time
def f(n):
   return n*n
if __name__=='__main__':
    t1=time.time()
    array=[1,2,3,4,5]
    p=Pool()
    result=p.map(f,array)
    print(result)
    p.close()
    p.join()