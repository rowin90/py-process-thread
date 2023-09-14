"""asyncio事件驱动使用"""

import asyncio
import time

now = lambda: time.time()


def event_handle(future):
    if (future):
        print("购买 '%s' 成功" % future.result())
    else:
        print('购买失败')


# 1. 定义函数
def buy(item):
    return item


start = now()

# 3. 获取默认的事件循环对象
loop = asyncio.get_event_loop()
# 4. 默认 buy 会在一个线程池中运行
future = loop.run_in_executor(None, buy, '电脑')

# 5. 设置回调函数，也就是 event——handle
future.add_done_callback(event_handle)

# 6. 启动事件循环
loop.run_until_complete(future)
print('耗时:', now() - start)
