from functools import reduce
import operator


def part_one(lines):
    limits = {'red': 12, 'green': 13, 'blue': 14}
    game_id_sum = 0
    for line in lines:
        valid_game = True
        id, moves = line.split(': ')
        # get game_id by splitting and indexing from the end
        game_id = id.split('Game ')[-1]
        for move in moves.split('; '):
            for amount, color in [single_move.split(' ') for single_move in move.split(', ')]:
                print(amount, color, limits[color])
                if limits[color] < int(amount):
                    valid_game = False
        if valid_game:
            game_id_sum += int(game_id)
    print(f"Sum Part One: {game_id_sum}")


def find_string_idx(searchstring, word):
    return int((searchstring.find(word)))


def part_two(lines):
    ans = 0
    for line in lines:
        max_cubes = {'red': 0, 'green': 0, 'blue': 0}
        id, moves = line.split(': ')
        # get game_id by splitting and indexing from the end
        game_id = id.split('Game ')[-1]
        for move in moves.split('; '):
            for amount, color in [single_move.split(' ') for single_move in move.split(', ')]:
                if max_cubes[color] < int(amount):
                    max_cubes[color] = int(amount)
        ans += reduce(operator.mul, max_cubes.values())
    print(f"Sum Part Two: {ans}")


with open("day_02/input.txt", "r") as input:
    text = input.read().rstrip()
    lines = text.splitlines()
    part_one(lines)
    part_two(lines)
