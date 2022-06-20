#!/usr/bin/python3

import threading
import time
import sys

def thread_func(i):
    if i == 1:
        for step in range(1,50,2):
            print("thread1: {}".format(step))
    else:
        for step in range(2,50,2):
            print("thread2: {}".format(step))
    time.sleep(10)
    return

t1 = threading.Thread(target=thread_func, args=(1,))
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_func, args=(2,))
t2.daemon = True
t2.start()

print("\nmain thread exit...")
sys.exit()