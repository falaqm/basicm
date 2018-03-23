''' error due to same name as multiprocessing'''
import multiprocessing

def calsqr(num,result,v):
    v.value=5.67
    for idx , n in enumerate(num):
        result[idx]=n*n
    print("result within process", result[:])


if __name__ == '__main__':
    arr = [2, 3, 8]
    result=multiprocessing.Array('i',3) #usingrray
    v=multiprocessing.Value('d', 0.0) #using value
    p = multiprocessing.Process(target=calsqr, args=(arr, result, v))
    p.start()
    p.join()

    print(result[:])
    print(v.value)
    print('done')

