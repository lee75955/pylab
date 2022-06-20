#!usr/bin/python3

import threading
import time
import sys

class MyThread(threading.Thread):
    def __init__(self, arg):
        threading.Thread.__init__(self)
        self.val = arg
    def run(self):
        if self.val == 1:
            for step in range(1, 50, 2):
                print("thread1: {}".format(step))
        else:
            for step in range(2, 50, 2):
                print("thread2: {}".format(step))
        time.sleep(10)
        return

t1 = MyThread(1)
t1.start()
t1.join()
print("----------------")

t2 = MyThread(2)
t2.start()