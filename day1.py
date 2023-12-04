import re


def day1(line_map=False):
    output_raw = []
    output_numbers = []
    result = int()
    # some of these little shits share characters...
    mapping = [
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "t3e"),
        ("four", "f4r"),
        ("five", "f5e"),
        ("six", "s6x"),
        ("seven", "s7n"),
        ("eight", "e8t"),
        ("nine", "n9e"),
        ("zero", "z0o"),
    ]

    with open("2023/day1.txt") as file:
        for line in file:
            if line_map:
                for item in mapping:
                    line = line.replace(item[0], item[1])
            output_raw.append(re.sub(r"\D", "", line))  # strip all letters
        for item in output_raw:
            output_numbers.append(str(item[0]) + str(item[-1]))
        for item in output_numbers:
            result = result + int(item)
    return result


print(day1())  # 54667
print(day1(True))  # 54203
