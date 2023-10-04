import time
initial_time = time.time()

history = {}
def generate_sequence(value):
    count = 0

    while (value != 1):
        if value % 2 == 0: 
            value = value // 2
        else:
            value = 3*value + 1

        count += 1

    return count  

biggest_value = 0
biggest_sequence_quantity = 0

for x in range(1, 1000000):
    sequence = generate_sequence(x)
    
    history[x] = sequence
    
    if (sequence > biggest_sequence_quantity):
        biggest_value = x
        biggest_sequence_quantity = sequence

print('-----------------------------')
print('Maior número é', biggest_value)
print('Gera',biggest_sequence_quantity ,'números')
print('-----------------------------')

print(time.time() - initial_time)