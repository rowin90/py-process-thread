import concurrent.futures
import multiprocessing
import multiprocessing as mp
from multiprocessing import Lock
import time

# multiprocessing.set_start_method('fork')

# 创建进程锁
lock = Lock()
print('lock 哟', id(lock))

# 定义共享资源
shared_resource = []
print('这是 shared_resource的', mp.current_process().name, id(shared_resource), shared_resource)

# a = 1
# print('a', mp.current_process().name, id(a), a)

# 定义需要执行的任务
def worker(index):
    # 在进程锁的上下文内访问共享资源
    with lock:
        # global a
        # a += 1
        # print('a', mp.current_process().name, id(a), a)
        shared_resource.append(index)
        # time.sleep(0.1)

        print('shared_resource',mp.current_process().name,id(shared_resource), shared_resource)


if __name__ == '__main__':
    print('开始')

    # 使用 ProcessPoolExecutor 并行执行任务
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(worker, i) for i in range(10)]

    # worker(1)

    # 打印共享资源
    print('主进程', mp.current_process().name, id(shared_resource), shared_resource)
    # print('主进程', mp.current_process().name, id(a), a)
