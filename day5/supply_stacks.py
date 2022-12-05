import re


input = "input.txt"

def stacks_maker(file):
    with open(file, "r") as f:
        lines = f.readlines()

    lines = lines[:lines.index('\n')]
    satcks_list = re.findall('(\d)', lines[-1])
    nb_stacks = int(satcks_list[-1])
    stacks = [[] for _ in range(nb_stacks)]
    for line in lines[:-1][::-1]: #[::-1] reverse list
        for i in range(nb_stacks):
            crate = line[i*4+1]
            if crate != ' ':
                stacks[i].append(crate)
    return stacks, nb_stacks

# Part. 1
move = False
stacks, nb_stacks = stacks_maker(input)

with open(input, "r") as f:
    for line in f:
        if line == '\n':
            move = True
            continue
        if move and len(line) != 0:
            to_move = int(line.split()[1])
            from_ = int(line.split()[3]) - 1
            to = int(line.split()[5]) - 1
            for _ in range(to_move):
                crate = stacks[from_][-1]
                stacks[from_].pop()
                stacks[to].append(crate)

result_1 = ''
for i in range(nb_stacks):
    result_1 += str(stacks[i][-1])
print(result_1)

# Part. 2
move = False
stacks, nb_stacks = stacks_maker(input)

with open(input, "r") as f:
    for line in f:
        if line == '\n':
            move = True
            continue
        if move and len(line) != 0:
            from_ = int(line.split()[3]) - 1
            to_move = len(stacks[from_]) - int(line.split()[1])
            to = int(line.split()[5]) - 1
            crates = stacks[from_][to_move:]
            stacks[from_] = stacks[from_][:to_move]
            stacks[to] += crates

result_2 = ''
for i in range(nb_stacks):
    result_2 += str(stacks[i][-1])
print(result_2)
