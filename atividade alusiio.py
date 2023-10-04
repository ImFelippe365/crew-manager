def generate_hash(x: int):
    return int(x) % 10

def insert(table, value):
    key = generate_hash(value)
    if not table.get(key):
        table[key] = value
        return
    
    new_value = table[key] if type(table[key]) is list else [table[key]]
    new_value.append(value)

    table[key] = new_value

def remove(table, key):
    if not table.get(generate_hash(key)): 
        return

    del table[generate_hash(key)]

def search_employeer(table, value):
    key = generate_hash(value)
    result = table.get(key)

    if type(result) is list:
        index = result.index(value)
        return result[index]
    
    return result

matricula = 1234567
hash_table = {
    generate_hash(matricula): 'Felippe R. Oliveira',
    generate_hash(200000): 'Ze neto',
    generate_hash(100000): 'Breno',
}

print("Tabela hash -> ",hash_table)
print("Resultado da busca -> ", search_employeer(hash_table, matricula))
insert(hash_table, 87654321)
# print("Tabela hash após inserir -> ",hash_table)
# remove(hash_table, matricula)
print("Tabela hash após remover -> ",hash_table)
insert(hash_table, 87654321)
print("Tabela hash após inserir no mesmo lugar -> ",hash_table)
print("Resultado da busca após inserir no mesmo lugar -> ", search_employeer(hash_table, 87654321))