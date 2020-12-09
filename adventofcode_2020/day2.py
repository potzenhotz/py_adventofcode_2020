from re import search, compile
from pathlib import Path

cwd = Path(__file__).resolve().parent
day_2_file = cwd.joinpath("data/day2.txt")

pattern = compile("([0-9]*)-([0-9]*)\s([a-z]):\s([a-z]*)")

with open(day_2_file, "r") as f:
    extracted_data = [pattern.search(lines).groups() for lines in f]


def meets_policy(input_tuple):
    count_of_string = input_tuple[3].count(input_tuple[2])
    return int(input_tuple[0]) <= count_of_string <= int(input_tuple[1])


def meets_policy_2(input_tuple):
    try:
        pos1 = input_tuple[3][int(input_tuple[0]) - 1] == input_tuple[2]
    except IndexError:
        pos1 = False
    try:
        pos2 = input_tuple[3][int(input_tuple[1]) - 1] == input_tuple[2]
    except IndexError:
        pos2 = False
    return pos1 != pos2


# Task 1
valid_passwords = list(filter(meets_policy, extracted_data))
sum_valid_passwords = len(valid_passwords)
print(sum_valid_passwords)

# Task 2
valid_passwords_2 = list(filter(meets_policy_2, extracted_data))
sum_valid_passwords_2 = len(valid_passwords_2)
print(sum_valid_passwords_2)

# use regex to parse into list of list
