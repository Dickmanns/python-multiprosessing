import time
import multiprocessing as mult

start = time.perf_counter()



def test():
    print('sleeping now ...')
    time.sleep(1)
    print('done sleeping')

if __name__ == '__main__':
    p1 = mult.Process(target = test)
    p2 = mult.Process(target = test)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} seconds(s)')