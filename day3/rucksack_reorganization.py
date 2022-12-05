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
        ascii_ = ord(common)
        if ascii_ > 96:
            ascii_ -= 96 # a(char) = 97(dec) - 1(place in alphabet)
        else:
            ascii_ -= 38 # A(char) = 65(dec) - 27(place in alphabet)
        sum += ascii_
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
            ascii_ = ord(common)
            if ascii_ > 96:
                ascii_ -= 96
            else:
                ascii_ -= 38
            sum += ascii_
            d1.clear()
            d2.clear()
print(sum)
