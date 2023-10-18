from multiprocessing import Process, Queue
import multiprocessing as mp


def worker(q):
    """子进程"""
    data = q.get()  # 从队列中获取数据
    print("Received:", data,mp.current_process().name)


if __name__ == "__main__":
    queue = Queue()  # 创建一个 Queue 对象

    p = Process(target=worker, args=(queue,))  # 创建子进程，并将队列作为参数传入
    p1 = Process(target=worker, args=(queue,))  # 创建子进程，并将队列作为参数传入
    p.start()  # 启动子进程
    p1.start()  # 启动子进程

    data = "Hello, World!"
    data1 = "Hello, World!1111"
    queue.put(data)  # 将数据放入队列中
    queue.put(data1)  # 将数据放入队列中
    # p.join()  # 等待子进程结束
    p1.join()  # 等待子进程结束
