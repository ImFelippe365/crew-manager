import names
import random


class Crew:
    def __init__(self, code, name, age, document):
        self.code = code
        self.name = name
        self.age = age
        self.document = document

class Ship:
    def __init__(self, ship_id):
        self.id = ship_id
        self.name = f'Navio {self.id}'
        self.crew = {}

    def is_full(self):
        return list(self.crew.values()) == 50

    def embark(self, crew):
        if self.is_full():
            return
        
        self.crew.update({generate_hash(crew.document): crew})

def generate_cpf():                                                        
    cpf = [random.randint(0, 9) for x in range(9)]                              
    
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
        
        cpf.append(11 - val if val > 1 else 0)                                  
        
    return int(''.join(map(str, cpf))) 

def generate_hash(x: int):
    return int(x) / 10

def generate_ship_hash(x: int):
    return int(x) * 1024

def insert(table, crew, ship_id):
    ship_hash_code = generate_ship_hash(ship_id)
    new_ship = Ship(ship_id) if not table.get(ship_hash_code) else table[ship_hash_code]
    new_ship.embark(crew)
    
    table[ship_hash_code] = new_ship

def search(table, ship_key, crew_id):
    crew_key = generate_hash(crew_id)

    ship = table.get(ship_key)
    crew = ship.crew.get(crew_key)
    
    return crew

hash_table = {}

for code in range(250):
    name = names.get_full_name()
    age = random.randint(18,40)
    
    new_crew = Crew(code + 1, name, age, generate_cpf())
    ship_id = code // 50
    
    insert(hash_table, new_crew, ship_id + 1)

while True:
    print('''
    0- Sair do programa
    
    1- Ver tripulação de um navio
    2- Pesquisar por tripulante
    3- Ver tripulação de todos os navios 
    
''')
    
    choice = int(input('Digite o número referente a opção que deseja realizar -> '))

    if choice == 0:
        print('-- Programa encerrado --')
        break

    if choice == 1:
        for ship in list(hash_table.values()):
            print(f'{ship.id}- {ship.name}')

        ship_choice = int(input('Digite o barco que deseja visualizar a tripulação: '))

        ship_id = generate_ship_hash(ship_choice)
        ship = hash_table.get(ship_id)

        if ship:
            print(f'---------------- {ship.name} ----------------')
            for crew in list(ship.crew.values()):
                code = crew.code
                name = crew.name
                age = crew.age
                document = crew.document

                print('-------------------')
                print(f'Código: {code}')
                print(f'Nome: {name}')
                print(f'Idade: {age} anos')
                print(f'CPF: {document}')
                print('-------------------')
            
            print('-----------------------------------------\n')
        else:
            print('Opção inválida')

    # if choice == 1:
    #     print('-- Vamos cadastrar um novo tripulante --')
    #     code = int(input('Digite o código do tripulante: '))
    #     name = input('Digite o nome: ')
    #     age = int(input('Digite a idade: '))

    #     insert(hash_table, {
    #         'code': code,
    #         'name': name,
    #         'age': age,
    #     })

    #     print('Tripulante cadastrado com sucesso!')

    elif choice == 2:
        for ship in list(hash_table.values()):
            print(f'{ship.id}- {ship.name}')

        ship_choice = int(input('Digite a opção correspondente ao barco que deseja visualizar a tripulação: '))

        ship_id = generate_ship_hash(ship_choice)
        ship = hash_table.get(ship_id)

        if ship:
            code = int(input('Digite o CPF do tripulante: '))
            result = search(hash_table, ship_id,  code)

            if not result:
                print('Não encontrado')
            else:
                print('\n\nResultado encontrado:\n')
            
                print(f'---------------- {ship.name} ----------------')
                code = result.code
                name = result.name
                age = result.age
                document = result.document
                
                print('-------------------')
                print(f'Código: {code}')
                print(f'Nome: {name}')
                print(f'Idade: {age} anos')
                print(f'CPF: {document}')
                print('-------------------')
            
                print('-----------------------------------------\n')
        else:
            print('Opção inválida')

        
    elif choice == 3:
        for ship in list(hash_table.values()):
            print(f'---------------- {ship.name} ----------------')
            
            for crew in list(ship.crew.values()):
                code = crew.code
                name = crew.name
                age = crew.age
                document = crew.document
                
                print('-------------------')
                print(f'Código: {code}')
                print(f'Nome: {name}')
                print(f'Idade: {age} anos')
                print(f'CPF: {document}')
                print('-------------------')

            print('-----------------------------------------\n')

    else:
        print('-- Opção inválida --')
    