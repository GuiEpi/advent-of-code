with open("input.txt", "r") as f:
    line = f.readline()

# Part. 1
def find_start_of_packet_marker(data):
    last_four = []

    for i, c in enumerate(data):
        last_four.append(c)
        if len(last_four) > 4:
            last_four.pop(0)

        if len(set(last_four)) == 4:
            return i + 1

    return -1


print(find_start_of_packet_marker(line))

# Part. 2
def find_start_of_message_marker(data):
    i = 0

    while i < len(data):
        if len(set(data[i : i + 14])) == 14:
            return i + 14
        i += 1

    return -1


print(find_start_of_message_marker(line))
