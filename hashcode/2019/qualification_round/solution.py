from math import inf
data = []
h_data = []
v_data = []
slideshow = []

with open('b_lovely_landscapes.txt', 'r') as inputs:
    nb_photos = int(inputs.readline().strip("\n"))
    for line in inputs:
        data.append(line.strip('\n').split(' '))

min_tags = inf
max_tags = 0

for i in range(len(data)):
    if data[i][0] == 'H':
        h_data.append([i, data[i][0], int(data[i][1]), {tag for tag in data[i][2:]}])
        if int(data[i][1]) > max_tags:
            max_tags = int(data[i][1])
        if int(data[i][1]) < min_tags:
            min_tags = int(data[i][1])
    elif data[i][0] == 'V':
        v_data.append([i, data[i][0], int(data[i][1]), {tag for tag in data[i][2:]}])
print("original data amount", len(h_data))

h_split = [[] for _ in range(5)]
for i in range(len(h_data)):
    a = (max_tags-min_tags)//5
    if h_data[i][2] < a:
        h_split[0].append(h_data[i])
    elif h_data[i][2] < 2*a and h_data[i][2] >= a:
        h_split[1].append(h_data[i])
    elif h_data[i][2] < 3*a and h_data[i][2] >= 2*a:
        h_split[2].append(h_data[i])
    elif h_data[i][2] < 4*a and h_data[i][2] >= 3*a:
        h_split[3].append(h_data[i])
    elif h_data[i][2] >= 4*a:
        h_split[4].append(h_data[i])
for splitted in h_split:
    if len(splitted) == 0:
        continue
    if len(splitted) <= 20:
        slideshow.append(splitted)
    while len(splitted) > 20:
        slideshow.append(splitted[:20])
        splitted = splitted[20:]
print("1st gen slideshow", len(slideshow))
slideshow2 = []
partner = []
current = []
score = 0
tmp_score = 0
for tenslides in slideshow:
    current = tenslides[0]
    partner = []
    slideshow2.append(current)
    tenslides.remove(current)
    while len(tenslides) > 0:
        for slide in tenslides:
            for tag in slide[3]:
                if tag in current[3]:
                    tmp_score += 1
            if abs(tmp_score - slide[2]//2) <= abs(score - slide[2]//2):
                score = tmp_score
                partner = slide
        slideshow2.append(partner)
        current = partner
        tenslides.remove(partner)
        score = 0
        tmp_score = 0

print("SLIDESHOW COMPLETE")

points = 0
for k in range(len(slideshow2)-1):
    tmp = 0
    for tag in slideshow2[k+1][3]:
        if tag in slideshow2[k][3]:
            tmp += 1
    points += min(min(slideshow2[k+1][2]-tmp, slideshow2[k][2]-tmp), tmp)

print(points)