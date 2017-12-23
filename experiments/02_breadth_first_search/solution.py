import psutil
import threading
import os
import time
import pathlib
import queue

def get_cpu_amount():
    return psutil.cpu_count()

path = "/home/tora"
q = queue.Queue(maxsize=0)
threads = []
substring = ".py"

def process(task):
    global lock_queue
    count = 0
    for i in os.listdir(task):
        p = os.path.join(task, i)
        if os.path.isdir(p):
            if os.access(p, os.R_OK):
                q.put(p)
        elif os.path.isfile(p):
            if i.find(substring) != -1:
                count += 1
    return count


def search(substring, queue, out, index):
    count = 0
    while True:
        task = queue.get()
        if task is None:
            break
        count += process(task)
        queue.task_done()
    out[index] = count

thread_count = 16

count = []

q.put(path)

for i in range(thread_count):
    count.append(0)
    thread = threading.Thread(target=search, args=(substring, q, count, i))
    threads.append(thread)
    thread.start()

q.join()

for i in range(thread_count):
    q.put(None)

for t in threads:
    thread.join()

print(sum(count))
