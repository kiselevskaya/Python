import psutil
import threading
import os
import time
import pathlib

def get_cpu_amount():
    return psutil.cpu_count()

path = "/home/tora"
lock = threading.Lock()

count = 0

def print_func(to_print, lock):
    global count
    lock.acquire()
    try:
        count += 1
#        print 'FILE\t{}'.format(to_print)
    finally:
        lock.release()

def search_for_file(path, substring, lock):
    threads = []
    for i in os.listdir(path):
        p = os.path.join(path, i)
        if os.path.isdir(p):
            access = (os.stat(p).st_mode & 0777)
            if access == 0775 or access == 0755:
                t1 = threading.Thread(target=search_for_file, args=(p, substring, lock))
                t1.start()
                threads.append(t1)
                #search_for_file(p, substring, lock)
        elif os.path.isfile(p):
            if i.find(substring) != -1:
                print_func(p, lock)
    for t in threads:
        t.join()

search_for_file(path, 'py', lock)

print (count)
