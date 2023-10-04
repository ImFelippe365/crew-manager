import random
import time
from random import sample

import sys 
sys.setrecursionlimit(10**6) 

random_sequence = sample(range(0, 10001), 10000)
# random_sequence = [random.randint(1, 10000) for _ in range(10000)]



# started_at = time.time()

# def bubble_sort(sequence):
#     wasSorted = False
#     while not wasSorted:
#         wasSorted = True
#         for index in range(len(sequence)-1):
#             if sequence[index] > sequence[index + 1]:
#                 old_number = sequence[index + 1]
#                 sequence[index + 1] = sequence[index]
#                 sequence[index] = old_number

#                 wasSorted = False
        
#     return sequence

# print(bubble_sort(random_sequence))
# print('Tempo para ordenar bubble sort -> ', time.time() - started_at)

def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):
    # para uma versão com partição aleatória
    # descomente as próximas três linhas:
    # from random import randrange
    # rand = randrange(ini, fim)
    # a[rand], a[fim - 1] = a[fim - 1], a[rand]
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] <= pivo:
            a[i], a[ini] = a[ini], a[i]
            ini += 1

    return ini - 1

a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
started_at = time.time()
print(quick_sort(random_sequence))

print('Tempo para ordenar quick sort -> ', time.time() - started_at)