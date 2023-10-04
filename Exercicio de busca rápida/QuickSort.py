import random
import time
import sys 
from random import sample
import psutil 

sys.setrecursionlimit(10**6) 

random_sequence = sample(range(0, 10001), 10000)
running_time = time.time()

def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] <= pivo:
            a[i], a[ini] = a[ini], a[i]
            ini += 1

    return ini - 1

quick_sort(random_sequence)
running_time = time.time() - running_time

print('Uso da CPU ->',  psutil.cpu_percent(interval=1), '%')

for proc in psutil.process_iter():
        try:
            # Aqui ele pega o nome do processo
            processName = proc.name()
            # print(processName)
            if processName == 'python.exe':
                print(processName , ' ::: ', proc.memory_info().vms/1000000, 'MB') # Esse último comando é para pegar o consumo de VMS pelo processo
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

print('Tempo para ordenar quick sort -> ', running_time)
