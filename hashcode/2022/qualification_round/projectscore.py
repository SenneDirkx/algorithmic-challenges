
def parse_input(filename):
    with open("./input_data/" + filename + '.in.txt') as inputs:
        data_strings = []
        for line in inputs:
            data_strings.append(line.strip().split(" "))
    nb_contributors = int(data_strings[0][0])
    nb_projects = int(data_strings[0][1])

    contributors = {}
    projects = {}

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
        skills = {}
        for i in range(nb_of_roles):
            skill_name = data_strings[line_number+i][0]
            skill_level = int(data_strings[line_number+i][1])
            skills[skill_name] = skill_level
        line_number += nb_of_roles
        proj_countr += 1
        projects[proj_name] = [days_to_completion, score, best_before, skills]
            
    return nb_contributors, nb_projects, contributors, projects

def sort_projects(projects):
    sorted_projects = []
    for pr in projects.keys():
        sorted_projects.append([pr,projects[pr][0], projects[pr][3]]
        )


def create_output(filename, data):
    with open("./output_data/" + filename + '.out.txt') as outputs:
        outputs.write("data")

def run_solution(filename):
    nb_projects, projects = parse_input(filename)
    availibility_dict = {0:contributors}

    # do magic
    print(projects)

    #create_output(filename, data)

def run():
    test = True
    if test:
        run_solution("a_an_example")
    else:
        filenames = ["a_an_example", "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"]
        for filename in filenames:
            run_solution(filename)

run()


#dictionay project = project name : dict(skill, level)
#dictionary contribrutor = name : dict(skill, level)
#dictionary met skills as key en level vb python 1, python2, etc en values van alle namen die deze skill hebben
#projects sorteer op laatste dag klaar van vroeg naar laat en dan op snelste klaar en later proberen op langste om te zien of er verschil in zit
