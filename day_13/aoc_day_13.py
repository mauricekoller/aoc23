def match_puzzle(puzzle):
    # check all vertical axis:
    for i in range(len(puzzle[0])-1):
        # move left and right, and check if symbols are always the same in each row
        # as soon as one symbol differs: False
        # Except if we run out of Symbols on one side: True
        all_match = True
        for row in puzzle:
            left_side = [char for char in row[i::-1]]
            right_side = [char for char in row[i+1:]]
            print(left_side,right_side)
            compared = [l==r for l,r in zip(left_side, right_side)]
            if not all(compared):
                all_match = False
                break
        if all_match:
            print(f"vertical at index {i+1}")
            print(left_side, right_side)
            return (i+1)
    # check all horizontal axis:
    for i in range(len(puzzle)-1):
        # move up and down, and check if symbols are always the same in each column
        # as soon as one symbol differs: False
        # Except if we run out of Symbols on one side: True
        all_match = True
        for column in range(len(puzzle[0])):
            chars_above = [row[column] for row in puzzle[i::-1]]
            chars_below = [row[column] for row in puzzle[i+1:]]
            compared = [l==r for l,r in zip(chars_above, chars_below)]
            if not all(compared):
                all_match = False
                break
        if all_match:
            print(f"horizontal at index {i+1}")
            print(chars_above)
            print(chars_below)
            return 100*(i+1)
    print(f"No match found!")
    print(puzzle)
    return 0


def part_one(text):
    puzzles = [[line for line in puzzle.split('\n')] for puzzle in text.split('\n\n')]
    total_sum = 0
    for puzzle in puzzles:
        total_sum += match_puzzle(puzzle)
        



    print(f"Result Part 1: {total_sum}")


def match_puzzle_p2(puzzle):
    h_size = len(puzzle[0])
    v_size = len(puzzle)
    # check all vertical axis:
    for i in range(h_size-1):
        # move left and right, and check if symbols are always the same in each row
        # as soon as one symbol differs: False
        # Except if we run out of Symbols on one side: True
        match_counter = 0
        for row in puzzle:
            left_side = [char for char in row[i::-1]]
            right_side = [char for char in row[i+1:]]
            compared = [l==r for l,r in zip(left_side, right_side)]
            if all(compared):
                match_counter +=1
        print(f"Index {i}: Matches: {match_counter} / {v_size}")
        if (v_size-match_counter) == 1:
            print(f"possible vertical match at index {i+1}")
            return (i+1)
    # check all horizontal axis:
    for i in range(v_size-1):
        # move up and down, and check if symbols are always the same in each column
        # as soon as one symbol differs: False
        # Except if we run out of Symbols on one side: True
        match_counter = 0
        for column in range(h_size):
            chars_above = [row[column] for row in puzzle[i::-1]]
            chars_below = [row[column] for row in puzzle[i+1:]]
            compared = [l==r for l,r in zip(chars_above, chars_below)]
            if all(compared):
                match_counter +=1
        print(f"Index {i}: Matches: {match_counter} / {h_size}")
        if (h_size-match_counter) == 1:
            print(f"possible horizontal match at index {i+1}")
            return 100*(i+1)
    print(f"No match found!")
    print(puzzle)
    return 0


def part_two(text):
    # Find next best soultion meaning: All but one row or column matches
    # If there are multiple "solutions" check which one only has a differnce of 1 between left/right up/down
    puzzles = [[line for line in puzzle.split('\n')] for puzzle in text.split('\n\n')]
    total_sum = 0
    for puzzle in puzzles:
        total_sum += match_puzzle_p2(puzzle)
        



    print(f"Result Part 2: {total_sum}")


with open("day_13/input.txt", "r") as input:
    text = input.read().rstrip()
    # lines = text.splitlines()
    # part_one(text)
    part_two(text)
