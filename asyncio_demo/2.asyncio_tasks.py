'''asyncio事件驱动使用'''

import asyncio
import time

now = lambda: time.time()


def event_handle(future):
    if (future):
        print("购买 '%s' 成功" % future.result())
    else:
        print('购买失败')

# 1. 定义协程函数：购买事件
async def buy(item):
    await asyncio.sleep(1) # 即使每次都 sleep 了 1s,整个执行结果，循环了3个task，结果还是执行了1s多，协程的优势
    return item

start = now()

# 3. 获取默认的事件循环对象
loop = asyncio.get_event_loop()
# 4. 根据协程对象创建task对象：注册事件event
tasks =[]
for i in ["电脑","手机","掌机"]:
    task = asyncio.ensure_future(buy(i))
    # 5. 设置回调函数，也就是 event——handle
    task.add_done_callback(event_handle)
    tasks.append(task)

# 6. 启动事件循环
loop.run_until_complete(asyncio.wait(tasks))
print(task)
print('耗时:',now() - start)
