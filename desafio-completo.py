history = {}

def generate_sequence(sequence, value):
    
    if value == 1:
        return sequence

    sequence.append(value)
    
    if (value in history):
        return sequence + history[value]
    
    history[value] = sequence

    if value % 2 == 0: 
        return generate_sequence(sequence, int(value/2))
    else:
        return generate_sequence(sequence, int(3*value + 1))    

biggest_value = 0

for x in range(1, 1000000):
    sequence = generate_sequence([], x)
    sequence_quantity = len(sequence)

    if (sequence_quantity > biggest_value):
        biggest_value = x

print('Maior número ->',biggest_value)