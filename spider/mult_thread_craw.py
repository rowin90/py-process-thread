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
