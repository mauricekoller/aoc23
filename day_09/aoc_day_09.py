def part_one(lines):
    total_sum = 0
    for line in lines:
        i = 0
        numbers = []
        numbers.append([int(number) for number in line.split()])
        while not all([number == 0 for number in numbers[i]]):
            differences = list(map(lambda x, y: y-x, numbers[i][:-1], numbers[i][1:]))
            numbers.append(differences)
            i += 1
        next_num = 0
        for differences in reversed(numbers[:-1]):
            current_last = differences[-1]
            next_num = next_num+current_last
        total_sum += next_num
    print(f"Sum Part One: {total_sum}")


def part_two(lines):
    total_sum = 0
    for line in lines:
        i = 0
        numbers = []
        numbers.append([int(number) for number in line.split()])
        while not all([number == 0 for number in numbers[i]]):
            differences = list(map(lambda x, y: y-x, numbers[i][:-1], numbers[i][1:]))
            numbers.append(differences)
            i += 1
        next_num = 0
        for differences in reversed(numbers[:-1]):
            current_first = differences[0]
            next_num = current_first - next_num
        total_sum += next_num
    print(f"Sum Part Two: {total_sum}")


with open("day_09/input.txt", "r") as input:
    text = input.read().rstrip()
    lines = text.splitlines()
    part_one(lines)
    part_two(lines)
