# Python 并发编程
# 单线程和多线程
- thread
```python
import blog_spider
import threading
import time


def single_thread():
    print('single thread begin')
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print('single thread end')

def muti_thread():
    print('muti thread begin')
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('muti thread end')

if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print('single cost :',end - start)

    start = time.time()
    muti_thread()
    end = time.time()
    print('muti cost :',end - start)

```
# 生产者和消费者
```python
import queue
import spider.blog_spider as blog_spider
import time
import random
import threading


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(threading.currentThread().name, f"craw {url}", "url_queue.size=", url_queue.qsize())
        time.sleep(random.randint(1, 2))

def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + '\n')
        print(threading.currentThread().name, f"results.size", len(results), "html_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for url in blog_spider.urls:
        url_queue.put(url)

    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw{idx}")
        t.start()

    fout = open("data.txt", "w")
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f"parse{idx}")
        t.start()

```
# 为什么要用多进程
![对比多进程和多线程使用](https://rowin90.github.io/images/py/why_process0807.png)

# 对比多进程和多线程使用
![对比多进程和多线程使用](https://rowin90.github.io/images/py/mutiprocess_thread.png)

```python
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [112272535095293] * 100


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))

    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread, cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread, cost:", end - start, "seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process, cost:", end - start, "seconds")

# single_thread, cost: 40.538614988327026 seconds
# multi_thread, cost: 40.512372970581055 seconds
# multi_process, cost: 11.588581800460815 seconds
```

# 线程池（进程池）
- 池化后，可以解决线程or进程创建，销毁的性能开销
- 创建多线程，两种方式
    - pool.map
        - 1. 顺序
        - 2. 资源提前准备好
    - pool.submit
        - 1. future.result() 拿到结果
        - 2. 也是顺序的
        - 3. concurrent.futures.as_completed 哪个线程先执行完，就先返回谁
```python
import concurrent.futures
import spider.blog_spider as blog_spider

# 线程池

#  pool.map 是顺序的，适用于固定的资源，资源要提前准备好 blog_spider.urls
#  future = pool.submit() 也是顺序的。 future.result 拿到结果
#  concurrent.futures.as_completed  无序的， 哪个先完成，返回哪个

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print('craw over')

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # 遍历方法一
    # for future,url in futures.items():
    #     print(url,future.result())

    # 遍历方法二 as_completed  无序
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())

```
# 启动Celery
```shell
 celery -A celery_task worker -l info
```
