def part_one(lines):
    calibration_sum = 0
    for line in lines:
        print(line)
        digits = [char for char in line if char.isdigit()]
        print(digits)
        line_sum = digits[0] + digits[-1]
        print(line_sum)
        calibration_sum += int(line_sum)
    print(f"Sum Part One: {calibration_sum}")


def find_string_idx(searchstring, word):
    return int((searchstring.find(word)))


def part_two(lines):
    str_2_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    calibration_sum = 0
    for line in lines:
        number_idx = {}

        # search strings:
        for str_digit, int_digit in str_2_int.items():
            # find all appearances
            line_idx = -1
            last_occurence = -1
            while line_idx < len(line):
                idx = find_string_idx(line[line_idx+1:len(line)], str_digit)
                if idx != -1:
                    line_idx = idx+last_occurence+1
                    number_idx[str(line_idx)] = int_digit
                    last_occurence = line_idx
                else:
                    break

        # search digits:
        for idx, char in enumerate(line):
            if char.isdigit():
                number_idx[str(idx)] = int(char)

        sorted_values = [value for key, value in dict(sorted(number_idx.items(), key=lambda x: int(x[0]))).items()]

        line_sum = f"{sorted_values[0]}{sorted_values[-1]}"
        calibration_sum += int(line_sum)
        print(line)
        print(sorted_values)
        print(line_sum)
    print(f"Sum Part Two: {calibration_sum}")


with open("day_01/input.txt", "r") as input:
    text = input.read().rstrip()
    lines = text.splitlines()
    part_one(lines)
    part_two(lines)
