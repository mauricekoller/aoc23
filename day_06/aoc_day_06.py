from functools import reduce


def part_one(lines):
    resultset = []
    times, distances = [[val for val in line.split(':')[1].split()] for line in lines]
    for i in range(len(times)):
        winning_oppotunities = 0
        max_time = int(times[i])
        min_distance = int(distances[i])
        for duration in range(max_time):
            speed = duration
            distance = (max_time-duration)*speed
            if (distance > min_distance):
                winning_oppotunities += 1
        resultset.append(winning_oppotunities)
    mult = reduce(lambda a, b: a*b, resultset)

    print(f"Sum Part One: {mult}")


def part_two(lines):
    resultset = []
    times, distances = [[val for val in line.split(':')[1].split()] for line in lines]
    winning_oppotunities = 0
    max_time = int(''.join(times))
    min_distance = int(''.join(distances))
    for duration in range(max_time):
        speed = duration
        distance = (max_time-duration)*speed
        if (distance > min_distance):
            winning_oppotunities += 1
    resultset.append(winning_oppotunities)
    mult = reduce(lambda a, b: a*b, resultset)

    print(f"Sum Part Two: {mult}")


with open("day_06/input.txt", "r") as input:
    text = input.read().rstrip()
    lines = text.splitlines()
    part_one(lines)
    part_two(lines)
