from collections import Counter


def part_one(text):
    # #: Rock that does not move and does not weigh anything
    # O: Rock that does move and has weight
    # .: Ground
    lines = [[char for char in line] for line in text.split('\n')]
    for li, line in enumerate(lines):
        for ci, char in enumerate(line):
            if char == 'O':
                # try to move the char as far upwards as possible:
                curr_line = li
                while curr_line > 0:
                    next_line = curr_line-1
                    if lines[next_line][ci] == '.':
                        lines[next_line][ci] = 'O'
                        lines[curr_line][ci] = '.'
                    else:
                        break
                    curr_line -= 1
    total_sum = 0
    for idx, line in enumerate(reversed(lines)):
        factor = idx+1
        symbol_count = Counter(line)['O']
        total_sum += factor*symbol_count
    print(f"Result Part 1: {total_sum}")


def cycle_lines(lines):
    # roll north:
    for li, line in enumerate(lines):
        for ci, char in enumerate(line):
            if char == 'O':
                # try to move the char as far upwards as possible:
                curr_line = li
                while curr_line > 0:
                    next_line = curr_line-1
                    if lines[next_line][ci] == '.':
                        lines[next_line][ci] = 'O'
                        lines[curr_line][ci] = '.'
                    else:
                        break
                    curr_line -= 1
    # for line in lines:
    #     print(''.join(line))
    # print()
    # roll west:
    for li, line in enumerate(lines):
        for ci, char in enumerate(line):
            if char == 'O':
                # try to move the char as far left as possible:
                curr_ci = ci
                while curr_ci > 0:
                    next_ci = curr_ci-1
                    if lines[li][next_ci] == '.':
                        lines[li][next_ci] = 'O'
                        lines[li][curr_ci] = '.'
                    else:
                        break
                    curr_ci -= 1
    # for line in lines:
    #     print(''.join(line))
    # print()
    # roll south:
    for li in range(len(lines)-1, -1, -1):
        for ci, char in enumerate(lines[li]):
            if char == 'O':
                # try to move the char as far upwards as possible:
                curr_line = li
                while curr_line < len(lines)-1:
                    next_line = curr_line+1
                    if lines[next_line][ci] == '.':
                        lines[next_line][ci] = 'O'
                        lines[curr_line][ci] = '.'
                    else:
                        break
                    curr_line += 1
    # for line in lines:
    #     print(''.join(line))
    # print()
    # roll east:
    for li, line in enumerate(lines):
        for ci in range(len(line)-1, -1, -1):
            char = line[ci]
            if char == 'O':
                # try to move the char as far left as possible:
                curr_ci = ci
                while curr_ci < len(line)-1:
                    next_ci = curr_ci+1
                    if lines[li][next_ci] == '.':
                        lines[li][next_ci] = 'O'
                        lines[li][curr_ci] = '.'
                    else:
                        break
                    curr_ci += 1
    # for line in lines:
    #     print(''.join(line))
    # print()
    return lines


def part_two(text):
    cycles = 1000000000
    # #: Rock that does not move and does not weigh anything
    # O: Rock that does move and has weight
    # .: Ground
    lines = [[char for char in line] for line in text.split('\n')]
    # cycle:
    already_seen = []
    remaining = 0
    for _ in range(cycles):
        lines = cycle_lines(lines)
        new_line = ''.join(char for line in lines for char in line)
        if new_line in already_seen:
            print(f"We're in a loop after cycle {_}")
            remaining = cycles % _+1
            break
        already_seen.append(new_line)
    for _ in range(remaining+1):
        lines = cycle_lines(lines)

    total_sum = 0
    for idx, line in enumerate(reversed(lines)):
        factor = idx+1
        symbol_count = Counter(line)['O']
        total_sum += factor*symbol_count
    print(f"Result Part 2: {total_sum}")


with open("day_14/input.txt", "r") as input:
    text = input.read().rstrip()
    # lines = text.splitlines()
    # part_one(text)
    part_two(text)
