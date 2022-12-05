# Part. 1
pair = 0

with open("input.txt", "r") as f:
    for line in f:
        elf1, elf2 = line.split(",")
        elf1_section1, elf1_section2 = elf1.split("-")
        elf2_section1, elf2_section2 = elf2.split("-")
        if int(elf1_section1) >= int(elf2_section1) and int(elf1_section2) <= int(
            elf2_section2
        ):
            pair += 1
        elif int(elf2_section1) >= int(elf1_section1) and int(elf2_section2) <= int(
            elf1_section2
        ):
            pair += 1
print(pair)

# Part. 2
overlaps = 0

with open("input.txt", "r") as f:
    for line in f:
        elf1, elf2 = line.split(",")
        elf1_section1, elf1_section2 = elf1.split("-")
        elf2_section1, elf2_section2 = elf2.split("-")
        if int(elf1_section1) <= int(elf2_section1) and int(elf1_section2) >= int(
            elf2_section1
        ):
            overlaps += 1
        elif int(elf2_section1) <= int(elf1_section1) and int(elf2_section2) >= int(
            elf1_section1
        ):
            overlaps += 1
print(overlaps)
