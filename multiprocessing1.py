''' error due to same name as multiprocessing'''
import time
import multiprocessing
result=[]
def calsqr(num):
    global result
    for n in num:
        time.sleep(5)
        print('square',n*n)
        result.append(n*n)
        print("result within process",result)
# def calcube(num):
#     for n in num:
#         time.sleep(5)
#         print('cube',str(n*n*n))
if __name__=='__main__':
    arr=[2,3,8,9]

    p1 = multiprocessing.Process(target=calsqr, args=(arr,))
    # p2 = multiprocessing.Process(target=calcube, args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()
    print('result', result)
    print('done')
