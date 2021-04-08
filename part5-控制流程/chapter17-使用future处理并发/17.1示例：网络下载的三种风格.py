"""
future指一种对象，表示异步执行的操作

依序下载，下载完一个图像将其保存在硬盘后才请求下一个图像
并发下载，几乎同时请求所有图像，每下载完一个文件就保存一个

编写并发代码经常这样重构：把依序执行的for循环体改成函数，以便并发调用

标准库有两个名为Future的类，concurrent.futures.Future和asyncio.Future，两个Future类的实例都表示可能已经完成或尚未完成的延迟计算
future封装待完成的操作，可以放入队列，完成的状态可以查询，得到结果后可以获取结果
通常情况下不应自己创建future,只能由并发框架实例化
future表示终将发生的事，确定某件事会发生的唯一方式是执行时间已经排定
客户端代码不应改变future的状态，并发框架在future表示的延迟计算结束后会改变future的状态，我们无法控制计算何时结束
客户端代码通常不会询问future是否运行结束，而是等待通知，.add_done_callback()方法，future运行结束后会调用指定的可调用对象

future.done() 不阻塞，返回布尔值，指明future链接的可调用对象是否已经执行
future.result(),在future运行结束后调用，返回可调用对象的结果。future没有运行结束，concurrent.futures.Future会阻塞调用方所在的线程直到有结果可返回
"""
# 依序下载脚本
import os
import time
import sys

import requests  # 不是标准库，依照惯例在导入标准库中的模块后导入，使用一个空行分开

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content  # 返回响应中的二进制内容


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower + '.gif')

    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


# 使用concurrent.futures模块下载
from concurrent import futures

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many1(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # 避免创建多余线程
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))  # 在多个线程中并发调用，map返回一个生成器，因此可以迭代获取各个函数的返回值

    return len(list(res))

# 演示future
def download_many2(cc_list):
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one,cc)  # 排定可调用对象的执行时间，返回一个future,表示这个待执行的操作
            to_do.append(future)
            msg = 'Scheduled for {}:{}'
            print(msg.format(cc,future))

        results = []
        for future in futures.as_completed(to_do):  #在future运行结束后产出future
            res = future.result()  # 此时调用future.result()绝不阻塞，因future由as_completed函数产出
            results.append(res)

        return len(results)