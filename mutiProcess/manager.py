import multiprocessing
import time


def task(d):
    d[2] = 2

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        d[1] = 0
        p = multiprocessing.Process(target=task, args=(d,))
        p.start()

        p.join()
        print(d)
