import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=3, percpu = False)

def get_mem():
    return float(psutil.virtual_memory().used) / psutil.virtual_memory().total

my_array = []

def add_vals(my_array):
    if len(my_array) >= 8:
        my_array.pop(0)
    my_array.append([time.strftime("%d %b %Y %H:%M:%S", time.gmtime()), get_cpu_usage(), get_mem()])

'''
n = 0
while n < 100:
    add_vals(my_array)
    n += 1
print (len(my_array))


print ("CPU\tMEM")
while True:
    print ('{}\t{}'.format(get_cpu_usage(), get_mem()))
    time.sleep(0)
'''
