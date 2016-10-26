# coding: utf-8

import multiprocessing
import threading


def dead_loop():
    x = 0
    while True:
        x ^= 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=dead_loop)
    t.start()
