from math import ceil
import random

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
    duration_simulation, nb_intersections, nb_streets, nb_cars, bonus_points = map(lambda string: int(string), data[0].strip(" \n").split(' '))

    # street = [ start_intersection , end_intersection , street_name , travel time ]
    streets = []
    for street_input in data[1:nb_streets + 1]:
        raw_street = street_input.strip(" \n").split(' ')
        for i in range(len(raw_street)):
            if i != 2:
                raw_street[i] = int(raw_street[i])
        streets.append(raw_street)

    # car_path = [ nb_streets , street_name1, street_name2...... ]
    car_paths = []
    for car_path_input in data[nb_streets+1:nb_cars + nb_streets + 1]:
        car_path = car_path_input.strip(" \n").split(' ')
        car_path[0] = int(car_path[0])
        car_paths.append(car_path)
    
    streets_to_duration = {}
    for street in streets:
        streets_to_duration[street[2]] = street[3]

    intersections_to_streets = {}
    for street in streets:
        end_intersection = street[1]
        street_name = street[2]
        if end_intersection in intersections_to_streets:
            intersections_to_streets[end_intersection].add(street_name)
        else:
            intersections_to_streets[end_intersection] = set()
            intersections_to_streets[end_intersection].add(street_name)
    
    class Car:
        def __init__(self, id, path):
            self.id = id
            self.to_go_on_street = 0
            self.path = path
        
        def advance(self):
            if self.to_go_on_street == 0:
                self.path.pop(0)
                if len(self.path) == 0:
                    self.to_go_on_street = -1
                else:
                    self.to_go_on_street = streets_to_duration[self.path[0]]
            else:
                self.to_go_on_street -= 1
    
    cars = []
    for i in range(len(car_paths)):
        cars.append(Car(i, car_paths[i][1:]))
    
    streets_to_cars_total = {}
    for car_path in car_paths:
        for street_index in range(1,len(car_path)):
            if car_path[street_index] in streets_to_cars_total:
                streets_to_cars_total[car_path[street_index]] +=1
            else: 
                streets_to_cars_total[car_path[street_index]] = 1
    
    streets_to_cars_timed = []
    for t in range(duration_simulation):
        streets_to_cars_timed.append({})
        for car in cars:
            if car.to_go_on_street == -1:
                continue
            if car.to_go_on_street == 0:
                current_street = car.path[0]
                if current_street in streets_to_cars_timed[t]:
                    streets_to_cars_timed[t][current_street] += 1
                else:
                    streets_to_cars_timed[t][current_street] = 1
            car.advance()
    
    schedules = []

    for intersection in intersections_to_streets:
        schedule = []


        if len(intersections_to_streets[intersection]) == 1:
            schedule.append(str(intersection)+'\n')
            schedule.append(str(len(intersections_to_streets[intersection]))+'\n')
            for street in intersections_to_streets[intersection]:
                schedule.append(street + ' ' + '1' + '\n')
            schedules.append(schedule)
        else:
            current_t = 0
            streets_added = 0
            unique_added_streets = set()
            all_driven_on_streets = set()
            while current_t < duration_simulation:
                for street_name in intersections_to_streets[intersection]:
                    if street_name in streets_to_cars_timed[current_t] and streets_to_cars_timed[current_t][street_name] > 0:
                        all_driven_on_streets.add(street_name)
                current_t += 1
            
            current_t = 0
            total_streets = len(all_driven_on_streets)
            # street_seq = [None for st in range(total_streets)]
            # while streets_added < total_streets and current_t < duration_simulation:
            #     #print("--")
            #     for street_name in all_driven_on_streets:
            #         if street_name in unique_added_streets:
            #             continue
                    
            #         if street_name in streets_to_cars_timed[current_t] and streets_to_cars_timed[current_t][street_name] >0:
            #             streets_added += 1
            #             unique_added_streets.add(street_name)
            #             index = current_t % total_streets
            #             while street_seq[index] is not None:
            #                 index = (index + 1) % total_streets
            #             street_seq[index] = street_name
            #             #print(street_seq)
            #             #schedule.append(street_name + ' ' + str(1) + '\n')
            #     current_t += 1
            street_seq = {}
            while current_t < duration_simulation:
                #print("--")
                for street_name in all_driven_on_streets:
                    if street_name in unique_added_streets:
                        continue
                    
                    if street_name in streets_to_cars_timed[current_t] and streets_to_cars_timed[current_t][street_name] >0:
                        if street_name not in street_seq:
                            street_seq[street_name] = [0 for st in range(total_streets)]
                        index = current_t % total_streets
                        street_seq[street_name][index] += 1
                        #print(street_seq)
                        #schedule.append(street_name + ' ' + str(1) + '\n')
                current_t += 1
            street_seq_total = [None for st in range(total_streets)]
            max_street_seq = []
            for street_index in street_seq:
                for h in range(len(street_seq[street_index])):
                    max_street_seq.append([street_index, h, street_seq[street_index][h]])
            max_street_seq.sort(key=lambda x: x[2], reverse=True)
            trav = 0
            added = set()
            while trav < len(max_street_seq):
                index = max_street_seq[trav][1]
                if max_street_seq[trav][0] not in added and street_seq_total[index] is None:
                    street_seq_total[index] = max_street_seq[trav][0]
                    added.add(max_street_seq[trav][0])
                    del max_street_seq[trav]
                elif max_street_seq[trav][0] in added:
                    del max_street_seq[trav]
                else:
                    trav += 1

            trav = 0
            while trav < len(max_street_seq):
                if max_street_seq[trav][0] in added:
                    del max_street_seq[trav]
                else:
                    index = max_street_seq[trav][1]
                    while street_seq_total[index] is not None:
                        index = (index + 1) % total_streets
                    street_seq_total[index] = max_street_seq[trav][0]
                    del max_street_seq[trav]

            for street_index in street_seq_total:
                schedule.append(street_index + ' ' + str(1) + '\n')
            if len(schedule) > 0:
                schedule = [str(intersection)+'\n'] + [str(len(schedule))+'\n'] + schedule
                schedules.append(schedule)



    # restrict search space to subspaces

    # find solution for subspace


    # add solutions together
    result = [str(len(schedules)) + '\n']
    for sched in schedules:
        for line in sched:
            result.append(line)

    # return solution

    return result

def main():
    filenames = ['a', 'b', 'c', 'd', 'e', 'f']
    #filenames = ['e']
    input_ext = '.txt'
    output_ext = '.out'
    for filename in filenames:
        input_data = parse_input(filename + input_ext)
        solution = get_solution(input_data)
        write_output(filename + output_ext, solution)
        print(f"File {filename} done!")

main()


#dict van (keys) intersect nummer met als values set met straat namen

#per intersections aantal straten bijhouden 
#per straat aantal autos dat er door moet
#als er bij intersection maar 1 straat -) altijd groen
#straat zonder auto's altijd rood

#idee 1: prioriteer straat met meeste auto's die minste andere straten blokt
#prioriteer auto's die minder straten moeten

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#tony pseudo voor straks
#                       intersect x 
#            licht 1                   licht 2
# t=0       waiting_list1           waiting_list2
# t=1       waiting_list1           waiting_list2
# t=2       waiting_list1           waiting_list2
# ...
# ...
# t=max       waiting_list1           waiting_list2

# optimale sequentie bepalen? 
# 1: bepaal voor elk tijdstip een 'waarde' van elk licht
# 2: bepaal een 'loopke' dat een best mogelijke score bepaald

# hoe bepalen we 1 en 2 ? 

# 1
# Bekijk de wachtrij van elk licht (auto1, auto2, ..., auto n)
# elke auto heeft een score afhankelijk van hoe ver deze is van zijn eindoel, onder 'ideale' omstandigheden (hoe dichter hoe meer punten)
# extra: een auto die onmogelijk nog zijn einddoel kan halen is nul punten waard. De score van elke auto neemt af naarmate deze verder is in de lijs(schalingsfactor x?)
# nota: hoe weten we waar welke auto staat te wachten? --> veronderstel dat elke auto een perfect pad volgt (iemand betere suggesties?)

# 2
# euhm weet ik nog niet maar lijkt me haalbaar 

# gewenste output is dus iets als:
# voor alle intersecties:
# intersectie x = [ [scorelicht1_t0,scorelicht2_t0], [scorelicht1_t1,scorelicht2_t1], ..., [scorelicht1_tmax,scorelicht2_tmax]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Stel 1 straat heeft te veel autos om in tijd te kunnen doen en 1 straat te weining dan straat met te weining negeren

