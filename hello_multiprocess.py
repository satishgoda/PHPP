# coding: utf-8

import os
import multiprocessing as mp
from multiprocessing import Process


def docs():
    # print docstring of APIs
    for name, value in mp.__dict__.items():
        if name[:2] == '__':
            continue
        print '-'*100
        print name, value.__doc__


def sub_proc(name):
    # 子进程要执行的代码
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=sub_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
