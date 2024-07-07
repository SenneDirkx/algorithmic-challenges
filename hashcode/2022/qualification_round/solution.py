
def parse_input(filename):
    with open("./input_data/" + filename + '.in.txt', 'r') as inputs:
        data_strings = []
        for line in inputs:
            data_strings.append(line.strip().split(" "))
    nb_contributors = int(data_strings[0][0])
    nb_projects = int(data_strings[0][1])

    contributors = {}
    projects = {}

    skills_to_contributors = {}

    line_number = 1
    contr_counter = 0
    while contr_counter < nb_contributors:
        contr_name = data_strings[line_number][0]
        contr_nb_skills = int(data_strings[line_number][1])
        line_number += 1
        contr_skills_counter = 0
        skills = {}
        while contr_skills_counter < contr_nb_skills:
            skill_name = data_strings[line_number][0]
            skill_level = int(data_strings[line_number][1])
            if (skill_name, skill_level) not in skills_to_contributors:
                skills_to_contributors[(skill_name, skill_level)] = set()
            skills_to_contributors[(skill_name, skill_level)].add(contr_name)
            skills[skill_name] = skill_level
            line_number += 1
            contr_skills_counter += 1
        contr_counter += 1
        contributors[contr_name] = skills

    proj_countr = 0
    while proj_countr < nb_projects:
        proj_name = data_strings[line_number][0]
        days_to_completion = int(data_strings[line_number][1])
        score = int(data_strings[line_number][2])
        best_before = int(data_strings[line_number][3])
        nb_of_roles = int(data_strings[line_number][4])
        line_number += 1
        skills = []
        for i in range(nb_of_roles):
            skill_name = data_strings[line_number+i][0]
            skill_level = int(data_strings[line_number+i][1])
            skills.append((skill_name, skill_level))
        line_number += nb_of_roles
        proj_countr += 1
        projects[proj_name] = [days_to_completion, score, best_before, skills]
            
    return nb_contributors, nb_projects, contributors, projects, skills_to_contributors

def sort_projects(projects):
    sorted_projects = []
    for pr in projects.keys():
        sorted_projects.append([pr,projects[pr][0], projects[pr][2]])
    sorted_projects.sort(key = lambda sorted_projects: sorted_projects[1])
    return sorted_projects


def create_output(filename, data):
    with open("./output_data/" + filename + '.out.txt', 'w') as outputs:
        outputs.write(str(len(data)) + "\n")
        for pro in data:
            outputs.write(pro[0] + "\n")
            outputs.write(" ".join(pro[1]) + "\n")


def remove_impossible_projects(projects, skills_to_cont):
    possible_project_names = []
    for project in projects.keys():
        goodproject = True
        skills = projects.get(project)[3]
        max_skills = {}
        for skill in skills:
            if skill[0] not in max_skills:
                max_skills[skill[0]] = skill[1]
            else:
                if max_skills[skill[0]] < skill[1]:
                    max_skills[skill[0]] = skill[1]
        for skill in max_skills:
            possible = False
            maxlvl = max_skills.get(skill)
            for (skill_name, skill_level) in skills_to_cont.keys():
                if skill_name == skill and int(skill_level) >= maxlvl:
                    possible = True
            if not possible:
                goodproject = False
                break 
        if goodproject:
            possible_project_names.append(project)
    result = {}
    for n in possible_project_names:
        result[n] = projects.get(n)
    
    return result  
        

def run_solution(filename):
    nb_contributors, nb_projects, contributors, projects, skills_to_cont = parse_input(filename)
    projects = remove_impossible_projects(projects,skills_to_cont)
    #projects = get_project_scores(projects)
    availibility_dict = {0:set()}

    for contr in contributors:
        availibility_dict[0].add(contr)


    # do magic
    # print(contributors, projects)
    # print(sort_projects(projects))

    #output = run_basic_bitch(projects, availibility_dict, skills_to_cont, contributors)
    # C: -1, 1, -0.1, 0.1, 0.1, 10
    output = run_more_advanced(projects, availibility_dict, skills_to_cont, contributors, -1, 1, -0.1, 0.1, 0.1, 10)

    create_output(filename, output)



#blijven itereren over alle projecten totdat er geen valid projecten meer zijn,
#een valid project is een project waar score van project - (huidige dag - ideale dag) > 0 of ideale dag <= huidige dag
# en er zijn mensen die het project kunnen uitvoeren vb project met python 5 kan niet als er niemand is met python skill 5 of hoger

# project = days to completion, score, best_before, skills
def run_more_advanced(projects, availibility_dict, skills_to_cont, allcontributors, p1, p2, p3, p4, c1, c2):
    result = []
    sorted_projects = sort_projects_antho_maxim(projects, p1, p2, p3, p4)
    #sorted_contributors = sort_contributors(allcontributors)
    day = 0
    counter = 0
    while len(sorted_projects) != 0 and counter <10000:
        # print(len(sorted_projects))
        # print(counter)
        counter +=1
        project_counter = 0
        while project_counter < len(sorted_projects):
            current_used_contributors = set()
            project_name = sorted_projects[project_counter]
            current_project = projects[project_name]
            # is dit nog een valid project, zo niet weg
            project_score = current_project[1]
            days_to_completion = current_project[0]
            ideal_day = current_project[2]
            project_overtime = day + days_to_completion - ideal_day
            is_worth_it = project_score - project_overtime > 0
            if not is_worth_it:
                del sorted_projects[project_counter]
                continue
            
            # zoek contributors
            current_skills = current_project[3]
            #print(current_skills)
            total_skills = len(current_skills)
            contributors = []
            for skill in current_skills:
                #print(skill)
                capable_contributors = set()
                skill_name = skill[0]
                skill_level = skill[1]
                for i in range(skill_level, skill_level+10):
                    if skills_to_cont.get((skill_name, i), None) != None:
                        capable_contributors.update(skills_to_cont.get((skill_name, i), None))
                #print(capable_contributors)
                if not capable_contributors:
                    if not find_mentor(skill_name, skill_level, contributors, allcontributors):
                        break
                    else:
                        lower_level_cont = skills_to_cont.get((skill_name, skill_level-1), None)
                        if not lower_level_cont:
                            break
                        else:
                            capable_contributors.update(lower_level_cont)
                if day not in availibility_dict:
                    break
                #print("test")
                #print(capable_contributors)
                #print(availibility_dict[day])
                capable_contributors = capable_contributors.intersection(availibility_dict[day])
                if not capable_contributors:
                    break
                #print("is avai")
                capable_cont_dict = {}
                for cap in capable_contributors:
                    capable_cont_dict[cap] = allcontributors[cap]
                
                sorted_contributors = sort_contributors_antho_maxim(capable_cont_dict, c1, c2)
                #print(sorted_contributors)

                i = 0
                cont = sorted_contributors[i]
                i += 1
                #cont = capable_contributors.pop()
                while cont in current_used_contributors and i < len(sorted_contributors):
                    cont = sorted_contributors[i]
                    i += 1
                
                if cont in current_used_contributors:
                    break

                
                contributors.append(cont)
                current_used_contributors.add(cont)
            #print(current_project_name, total_skills, len(contributors))
            if (len(contributors) == total_skills):
                result.append((project_name, contributors))
                for cont in contributors:
                    availibility_dict[day].remove(cont)
                    next_available = day + days_to_completion
                    if next_available not in availibility_dict:
                        availibility_dict[next_available] = set()
                    availibility_dict[next_available].add(cont)
                del sorted_projects[project_counter]
                

            # als gevonden, weg
            
            # zo niet, next project
            project_counter += 1

        next_day = day+1
        next_day = list(availibility_dict.keys())
    
        next_day.remove(day)
        if not next_day:
            break
        next_day = min(next_day)
        
        
        availibility_dict[next_day] = availibility_dict[day].union(availibility_dict[next_day])
        del availibility_dict[day]
        day = next_day
        
    return result
    
    
def run_basic_bitch(projects, availibility_dict, skills_to_cont, allcontributors):
    sorted_projects = sort_projects(projects)
    result = []
    used_contributors = set()
    for i in sorted_projects:
        current_used_contributors = set()
        current_project_name = i[0]
        current_skills = projects[current_project_name][3]
        total_skills = 0
        for sk in current_skills:
            sk_tot = len(current_skills[sk])
            total_skills += sk_tot
        contributors = []
        not_possible = False
        check_skill_after = []
        for skill in current_skills.keys():
            levels = current_skills[skill]
            capable_contributors = set()
            for level in levels:
                for i in range(level, level+10):
                    if skills_to_cont.get((skill, i), None) != None:
                        capable_contributors.update(skills_to_cont.get((skill, i), None))
                if not capable_contributors:
                    if not find_mentor(skill, level, contributors, allcontributors):
                        not_possible = True
                        break
                    else:
                        lower_level_cont = skills_to_cont.get((skill, level-1), None)
                        if not lower_level_cont:
                            not_possible = True
                            break
                        else:
                            capable_contributors.update(lower_level_cont)
                            


                cont = capable_contributors.pop()
                while capable_contributors and (cont in current_used_contributors or cont in used_contributors):
                    cont = capable_contributors.pop()
                
                if cont in current_used_contributors or cont in used_contributors:
                    not_possible = True
                    break
                
                contributors.append(cont)
                current_used_contributors.add(cont)
            if not_possible:
                break
        #print(current_project_name, total_skills, len(contributors))
        if (len(contributors) == total_skills):
            used_contributors.update(current_used_contributors)
            result.append((current_project_name, contributors))
        current_used_contributors = set()
    
    return result


def find_mentor(skill, level, current_team, contributors):
    for person in current_team:
        skills = contributors[person]
        found_level = skills.get(skill, None)
        if found_level and found_level >= level:
            return True
    return False

def get_person_scores(contributors, c1, c2):
    nb_talen_min = 0
    nb_talen_max = 0
    nb_averages_min = 0
    nb_averages_max = 0
    for person in contributors:
        l = contributors[person]
        nb_talen_min = len(l)
        nb_talen_max = len(l)
        for score in l:
            current_score = 0
            current_score += l[score]
        average_score = current_score/len(l)
        nb_average_min = average_score
        nb_average_max = average_score
        break

    for person in contributors:
        l = contributors[person]
        if len(l) < nb_talen_min:
            nb_talen_min = len(l)
        if len(l) > nb_talen_max:
            nb_talen_max = len(l)

        current_score = 0
        for score in l:
            current_score += l[score]
        average_score = current_score/len(l)
        if average_score < nb_average_min:
            nb_average_min = average_score
        if average_score > nb_average_max:
            nb_average_max = average_score

    personscores ={}
    for person in contributors:
        l = contributors[person]
        if (nb_talen_max-nb_talen_min) == 0:
            nb_talen = 0
        else:
            nb_talen = (len(l)-nb_talen_min)/(nb_talen_max-nb_talen_min)

        for score in l:
            current_score = 0
            current_score += l[score]
        
        if len(l) == 0:
            average_score = 0
        else:
            average_score = current_score/len(l)

        if (nb_average_max - nb_average_min) == 0:
            average = 0
        else:
            average = (average_score - nb_average_min)/ (nb_average_max - nb_average_min)

        nb_talen_weight = c1#1
        average_weight = c2#1
        person_score = (nb_talen * nb_talen_weight) + (average * average_weight)
        personscores[person] = person_score

    return personscores

        


def get_project_scores(projects, p1, p2, p3, p4):
    nb_days_min = 0
    nb_days_max = 0
    nb_points_min = 0
    nb_points_max = 0
    nb_best_before_min = 0
    nb_best_before_max = 0
    nb_persons_min = 0
    nb_persons_max = 0
    for project in projects:
        l = projects[project]
        nb_days_min = l[0]
        nb_days_max = l[0]
        nb_points_min = l[1]
        nb_points_max = l[1]
        nb_best_before_min = l[2]
        nb_best_before_max = l[2]
        nb_persons_min = len(l[3])
        nb_persons_max = len(l[3])
        break
        
    for project in projects:
        l = projects[project]
        if l[0] < nb_days_min:
            nb_days_min = l[0]
        if l[0] > nb_days_max:
            nb_days_max = l[0]

        if l[1] < nb_points_min:
            nb_points_min = l[1]
        if l[1] > nb_points_max:
            nb_points_max = l[1]

        if l[2] < nb_best_before_min:
            nb_best_before_min = l[2]
        if l[2] > nb_best_before_max:
            nb_best_before_max = l[2]

        if len(l[3]) < nb_persons_min:
            nb_persons_min = len(l[3])
        if len(l[3]) > nb_persons_max:
            nb_persons_max = len(l[3])

    projectscores = {} 
    for project in projects:
        l = projects[project]
        if (nb_days_max-nb_days_min) == 0:
            day_score = 0
        else:
            day_score = (l[0] - nb_days_min)/(nb_days_max-nb_days_min)
        if (nb_points_max-nb_points_min) == 0:
            nb_points_score = 0
        else:
            nb_points_score = (l[1] - nb_points_min)/(nb_points_max-nb_points_min)
        if (nb_best_before_max-nb_best_before_min) == 0:
            best_before_score = 0
        else:
            best_before_score = (l[2] - nb_best_before_min)/(nb_best_before_max-nb_best_before_min)
        if (nb_persons_max-nb_persons_min) == 0:
            persons_score = 0
        else:
            persons_score = (len(l[3])-nb_persons_min)/(nb_persons_max-nb_persons_min)

        day_score_weight = p1 #-1.5
        nb_points_score_weight = p2 #1.5
        best_before_score_weight = p3 #-1
        persons_score_weight = p4 #1

        projectscore = (day_score * day_score_weight) + (nb_points_score * nb_points_score_weight) + (best_before_score * best_before_score_weight) + (persons_score * persons_score_weight)
        projectscores[project] = projectscore
    return projectscores

        
def sort_projects_antho_maxim(projects, p1, p2, p3, p4):
    project_scores = get_project_scores(projects, p1, p2, p3, p4)
    #print("scores", project_scores)
    names = list(projects.keys())
    return sorted(names, key=lambda x: project_scores[x], reverse=True)

def sort_contributors_antho_maxim(contributors, c1, c2):
    contributor_scores = get_person_scores(contributors, c1, c2)
    #print("scores", contributor_scores)
    names = list(contributors.keys())
    return sorted(names, key=lambda x: contributor_scores[x])

def calc_result_score(output, projects):
    scores = map(lambda p: projects[p[0]][1], output)
    return sum(scores)

def validate_solution(filename):
    nb_contributors, nb_projects, contributors, projects, skills_to_cont = parse_input(filename)
    projects = remove_impossible_projects(projects,skills_to_cont)
    #projects = get_project_scores(projects)
    
    p1_options = [-0.1, -1, -10]
    p2_options = [0.1, 1, 10]
    p3_options = [-0.1, -1, -10]
    p4_options = [0.1, 1, 10]
    c1_options = [0.1, 1, 10]
    c2_options = [0.1, 1, 10]

    best_result = 0
    best_p1 = 0
    best_p2 = 0
    best_p3 = 0
    best_p4 = 0
    best_c1 = 0
    best_c2 = 0


    for p1 in p1_options:
        for p2 in p2_options:
            for p3 in p3_options:
                for p4 in p4_options:
                    for c1 in c1_options:
                        for c2 in c2_options:
                            availibility_dict = {0:set()}
                            for contr in contributors:
                                availibility_dict[0].add(contr)
                            output = run_more_advanced(projects, availibility_dict, skills_to_cont, contributors, p1, p2, p3, p4, c1, c2)
                            score = calc_result_score(output, projects)
                            #print(score)
                            if score > best_result:
                                best_result = score
                                best_p1 = p1
                                best_p2 = p2
                                best_p3 = p3
                                best_p4 = p4
                                best_c1 = c1
                                best_c2 = c2
                                print("New best:", best_result, "with p1", p1, "p2", p2, "p3", p3, "p4", p4, "c1", c1, "c2", c2)
    print("FINAL best:", best_result, "with p1", best_p1, "p2", best_p2, "p3", best_p3, "p4", best_p4, "c1", best_c1, "c2", best_c2)

def run():
    test = False
    validate_parameters = False
    if test:
        run_solution("c_collaboration")
    elif validate_parameters:
        validate_solution("c_collaboration")
    else:
        filenames = ["a_an_example", "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"]
        for filename in filenames:
            run_solution(filename)
            print("done")

run()


#dictionay project = project name : dict(skill, level)
#dictionary contribrutor = name : dict(skill, level)
#dictionary met skills as key en level vb python 1, python2, etc en values van alle namen die deze skill hebben
#projects sorteer op laatste dag klaar van vroeg naar laat en dan op snelste klaar en later proberen op langste om te zien of er verschil in zit
