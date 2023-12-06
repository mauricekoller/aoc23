from functools import reduce
import math


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


def Mitternachtsformel(a, b, c):
    x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    y = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    return x, y


def part_two(lines):
    resultset = []
    times, distances = [[val for val in line.split(':')[1].split()] for line in lines]
    winning_oppotunities = 0
    max_time = int(''.join(times))
    min_distance = int(''.join(distances))
    x, y = Mitternachtsformel(-1, max_time, -min_distance)
    lower_bound = math.ceil(min(x, y))
    upper_bound = math.floor(max(x, y))
    print(f"Sum Part Two: {upper_bound-lower_bound+1}")


with open("day_06/input.txt", "r") as input:
    text = input.read().rstrip()
    lines = text.splitlines()
    part_one(lines)
    part_two(lines)
