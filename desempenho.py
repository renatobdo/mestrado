import psutil
import os
import csv
import time
from datetime import datetime

def tempo():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def get_CPU_Usage():
    return psutil.cpu_percent()


def get_Memory_Usage():
    #total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    return round((used_memory/total_memory) * 100, 2)

#def get_networkbandwith():
#    total_net, used_memory, free_memory = map(int, os.popen('ifstat -t').readlines()[0].split()[1:])
#    return round((used_memory/total_memory) * 100, 2)

def get_net_io():
    return psutil.net_io_counters()
 
def disk_usage():
    return (psutil.disk_usage('/'))

def disk_io_counters(): 
    return (psutil.disk_io_counters(perdisk=False, nowrap=True))

while True:
    tempo1 = tempo()
    cpu1 = get_CPU_Usage
    ram1 = get_Memory_Usage
    print('tempo: ',tempo(),', cpu: ',get_CPU_Usage(),', ram: ',get_Memory_Usage(),', net_io_counters: ', get_net_io(), ', disk_usage: ',disk_usage(),', disk_io_counters: ', disk_io_counters())
   
    arquivo_log = open('/home/ubuntu/testes2/log.csv', mode='a')
    log = tempo(),get_CPU_Usage(),get_Memory_Usage(), get_net_io(), disk_usage(),disk_io_counters()
    arquivo_log.write(str(log)+'\n')
    time.sleep(3)
