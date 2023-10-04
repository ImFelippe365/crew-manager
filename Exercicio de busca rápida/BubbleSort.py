import time
from random import sample
import sys 

sys.setrecursionlimit(10**6) 

random_sequence = sample(range(0, 10001), 10000)

started_at = time.time()

def bubble_sort(sequence):
    wasSorted = False
    while not wasSorted:
        wasSorted = True
        for index in range(len(sequence)-1):
            if sequence[index] > sequence[index + 1]:
                old_number = sequence[index + 1]
                sequence[index + 1] = sequence[index]
                sequence[index] = old_number

                wasSorted = False
        
    return sequence

bubble_sort(random_sequence)
print('Tempo para ordenar bubble sort -> ', time.time() - started_at)