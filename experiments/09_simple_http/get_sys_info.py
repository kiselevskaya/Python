import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=3, percpu = False)

def get_mem():
    return float(psutil.virtual_memory().used) / psutil.virtual_memory().total

my_array = []

def add_vals(my_array):
    if len(my_array) > 8:
        my_array.pop(0)
    my_array.append([time.strftime("%d %b %Y %H:%M:%S", time.gmtime()), get_cpu_usage(), get_mem()])
