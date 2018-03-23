''' error due to same name as multiprocessing'''
import multiprocessing
result=[]
def calsqr(num,q):

    for n in num:
       q.put(n*n)

if __name__ == '__main__':
    arr = [2, 3, 8]
    q=multiprocessing.Queue()
    p = multiprocessing.Process(target=calsqr, args=(arr,q))
    p.start()
    p.join()

    while q.empty() is False:
        print('outside the process',q.get())
    print('done')

