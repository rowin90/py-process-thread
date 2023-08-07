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
