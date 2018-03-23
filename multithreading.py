import time
import threading
def calsquare(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square',n*n)
def calcube(numbers):
    print("calculate cube")
    for n in numbers:
        time.sleep(0.2)
        print('cube',n*n*n)
arr=[2,3,8,9]
t=time.time()
t1=threading.Thread(target=calsquare,args=(arr,))
t2=threading.Thread(target=calcube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print('done in:',time.time()-t)
