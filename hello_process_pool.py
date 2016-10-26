# coding: utf-8

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.clock()
    time.sleep(random.randint(3, 7))
    end = time.clock()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # Pool的默认大小是CPU的核数
    for i in range(5):
        """
        apply(object[, args[, kwargs]]) -> value

        Call a callable object with positional arguments taken from the tuple args,
        and keyword arguments taken from the optional dictionary kwargs.
        Note that classes are callable, as are instances with a __call__() method.

        Deprecated since release 2.3. Instead, use the extended call syntax:
            function(*args, **keywords).
        """
        # Asynchronous equivalent of `apply()` builtin
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')
    # Prevents any more tasks from being submitted to the pool.
    # Once all the tasks have been completed the worker processes will exit.
    p.close()
    # Wait for the worker processes to exit. One must call close() or terminate() before using join().
    p.join()
    print('All subprocesses done.')
