# coding: utf-8

"""
Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
"""
import threading

import time


def loop():
    # 新线程执行的代码:
    print('thread %s is running...' % threading.current_thread().name)
    for n in range(5):
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
# It must be called at most once per thread object.
t.start()

time.sleep(1)  # avoid mix output
print('thread %s will wait for child thread to exit.' % threading.current_thread().name)
t.join()
print('thread %s ended.' % threading.current_thread().name)
