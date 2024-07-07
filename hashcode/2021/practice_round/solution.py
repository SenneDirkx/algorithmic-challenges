def parse_input(filename):
    data = None
    with open(filename, 'r') as file:
        data = file.readlines()
    return data

def write_output(filename, data):
    with open(filename, 'w') as file:
        file.writelines(data)

def get_solution(data):
    # parse data
    pizza_amount, duos, trios, quadras = map(lambda str: int(str), data[0].strip(' \r\n').split(' '))
    pizzas = map(lambda pizza: pizza[1:],data[1:])

    delivered = []

    # restrict search space to subspaces
    # duos
    counter = 0
    while counter < min(2*duos,pizza_amount)-1:
        delivered.append(f"2 {counter} {counter+1}\n")
        counter += 2

    # trios
    while counter < min(2*duos+3*trios,pizza_amount)-2:
        delivered.append(f"3 {counter} {counter+1} {counter+2}\n")
        counter += 3
    
    # quadras
    while counter < min(2*duos+3*trios+4*quadras,pizza_amount)-3:
        delivered.append(f"4 {counter} {counter+1} {counter+2} {counter+3}\n")
        counter += 4

    # add solutions together


    # return solution
    return [str(len(delivered))+'\n'] + delivered

def main():
    filenames = ['a', 'b', 'c', 'd', 'e']
    input_ext = '.in'
    output_ext = '.out'
    for filename in filenames:
        input_data = parse_input(filename + input_ext)
        solution = get_solution(input_data)
        write_output(filename + output_ext, solution)

main()