'''Part. 1
A, X = Rock; score += 1
B, Y = Paper; score += 2
C, Z = Scissors; score += 3
lose = 0, draw = 3, win = 6
'''
score = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        opponent, me = line.split()

        if me == "X":
            if opponent == "A":
                score += 3
            if opponent == "C":
                score += 6
            score += 1

        if me == "Y":
            if opponent == "A":
                score += 6
            if opponent == "B":
                score += 3
            score += 2

        if me =="Z":
            if opponent == "B":
                score += 6
            if opponent == "C":
                score += 3
            score += 3

print(score)

'''Part. 2
A = Rock; score += 1
B = Paper; score += 2
C = Scissors; score += 3
lose = X = 0; draw = Y = 3; win = Z = 6
'''
score = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        opponent, me = line.split()

        if me == "X":
            if opponent == "A":
                score += 3
            if opponent == "B":
                score += 1
            if opponent == "C":
                score += 2
            score += 0

        if me == "Y":
            if opponent == "A":
                score += 1
            if opponent == "B":
                score += 2
            if opponent == "C":
                score += 3
            score += 3

        if me =="Z":
            if opponent == "A":
                score += 2
            if opponent == "B":
                score += 3
            if opponent == "C":
                score += 1
            score += 6

print(score)