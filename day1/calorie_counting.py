# Part. 1
total_calories = []
count = 0

with open("input.txt", "r") as f:
    for line in f:
        if line != "\n":
            count += int(line)
        total_calories.append(count)
        count = 0

max_calories = max(total_calories)
print(max_calories)

# Part. 2
top_three_elves = 0

for i in range(3):
    top_three_elves += max(total_calories)
    total_calories.remove(max(total_calories))

print(top_three_elves)
