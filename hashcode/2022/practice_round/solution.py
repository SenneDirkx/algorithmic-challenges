from typing import Dict, List, Set, Tuple

def parse_file(filename: str):
    store = {}
    clients = []
    with open(filename, 'r') as input_file:
        potential_clients = int(input_file.readline().strip())
        for _ in range(potential_clients):
            likes = input_file.readline().strip().split()[1:]
            for like in likes:
                if like in store:
                    store[like] += 1
                else:
                    store[like] = 1

            dislikes = input_file.readline().strip().split()[1:]
            for dislike in dislikes:
                if dislike in store:
                    store[dislike] -= 1
                else:
                    store[dislike] = -1
            
            clients.append((set(likes), set(dislikes)))
    
    return store, clients

def create_output(store: Dict, filename: str):
    ingredients = []
    for ing in store:
        if store[ing] >= 1:
            ingredients.append(ing)
    
    with open(filename[:-6] + "out", 'w') as output_file:
        output_file.write(str(len(ingredients)))
        output_file.write(" ")
        output_file.write(" ".join(ingredients))
    
    return ingredients

def check_performance(ingredients: List, clients: List):
    set_ing = set(ingredients)
    total = 0
    for client in clients:
        if check_client(set_ing, client):
            total += 1
    
    return total

def check_client(ingredients: Set, client: Tuple):
    for like in client[0]:
        if like not in ingredients:
            return False
    
    for dislike in client[1]:
        if dislike in ingredients:
            return False
    
    return True

files = ['a_an_example.in.txt', 'b_basic.in.txt', 'c_coarse.in.txt', 'd_difficult.in.txt', 'e_elaborate.in.txt']

for file in files:
    filename = './input_data/' + file
    store_file, potential_clients_file = parse_file(filename)
    result_ingredients = create_output(store_file, filename)
    total = check_performance(result_ingredients, potential_clients_file)
    print(file, ":", total, "/", len(potential_clients_file))
    

