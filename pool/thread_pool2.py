import time
import random
from concurrent.futures  import  ThreadPoolExecutor


# 线程池
def task(video_url):
    print('开始',video_url)
    time.sleep(2)
    return random.randint(0,10)

def done(response):
    print('执行',response.result())

pool = ThreadPoolExecutor(10)

url_list = ["www-{}.com".format(i) for i in range(15)]

for url in url_list:
    future = pool.submit(task,url)
    future.add_done_callback(done)

# 主线程等待线程池执行完
# pool.shutdown(True)
print('主线程执行完')
