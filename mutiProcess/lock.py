"""
锁也会被多进程中 在 fork 模式下，拷贝走。都是被进程中的主线程拷贝走
"""
import multiprocessing
import threading
import time


def func():
    print('来了')
    with lock:
        print(666)
        time.sleep(1)


def task():
    # 拷贝的时候锁也是被申请走的状态
    # 是被子进程中的主线程申请走了
    for i in range(10):
        t = threading.Thread(target=func)  # 这里面在子进程中开启了多线程，其实在子进程的，主线程里已经拷贝了一个锁了，如果没有释放，则子进程中的多线程会被 lock住
        t.start()
    # lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')

    name = []
    lock = threading.RLock()
    lock.acquire()

    p1 = multiprocessing.Process(target=task)

    p1.start()
