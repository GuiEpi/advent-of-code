priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}
# Part. 1
sum = 0

with open("input.txt", "r") as f:
    for line in f:
        item = line.rstrip()
        first_compartment, second_compartment = (
            item[: len(item) // 2],
            item[len(item) // 2 :],
        )
        d = {}
        for types in first_compartment:
            if types in d:
                d[types] += 1
            else:
                d[types] = 1
        common = ""
        for types in second_compartment:
            if types in d:
                common += types
                break
        sum += priorities[common]
print(sum)

# Part. 2
sum = 0
counter = 0
d1 = {}
d2 = {}

with open("input.txt", "r") as f:
    for line in f:
        item = line.rstrip()
        counter += 1
        if counter == 1:
            for types in item:
                if types in d1:
                    d1[types] += 1
                else:
                    d1[types] = 1
        if counter == 2:
            for types in item:
                if types in d2:
                    d2[types] += 1
                else:
                    d2[types] = 1
        if counter == 3:
            counter = 0
            common = ""
            for types in item:
                if types in d1 and types in d2:
                    common += types
                    break
            sum += priorities[common]
            d1.clear()
            d2.clear()
print(sum)
