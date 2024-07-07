data = []

with open('e_also_big.in', 'r') as inputs:
    for line in inputs:
        data.append(list(map(int, line.strip("\n").split(" "))))

M = data[0][0]
N = data[0][1]
types = data[1]

results = []
total = 0

for t in range(len(types) - 1, -1, -1):
    if total + types[t] <= M:
        total += types[t]
        results.append(t)

result = [f"{len(results)}\n", " ".join(list(map(str, results[::-1])))]

assert total < M

with open('e_also_big.out', 'w') as output:
    output.writelines(result)