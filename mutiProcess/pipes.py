import multiprocessing
import time


def task(conn):
    time.sleep(1)
    conn.send([111, 222])
    data = conn.recv()  # 阻塞
    print('子进程', data)
    time.sleep(1)

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=task, args=(child_conn,))
    p.start()

    info = parent_conn.recv()
    print('主进程', info)
    parent_conn.send(666)
