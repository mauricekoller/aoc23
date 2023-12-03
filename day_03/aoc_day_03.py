from functools import reduce
import operator


def part_one(lines):
    part_num_sum = 0

    lines_count = len(lines)

    previous_line = ''

    previous_symbols = []
    current_symbols = []
    next_symbols = []

    current_digits = []

    for i in range(lines_count):
        seen_ids = []
        previous_symbols = get_symbol_ids(previous_line)
        current_line = lines[i]
        current_symbols = get_symbol_ids(current_line)
        current_digits = get_digit_ids(current_line)
        next_line = lines[i+1] if i+1 < lines_count else ''
        next_symbols = get_symbol_ids(next_line)
        # check all numbers in current line
        # if they are adjacent to a symbol on the previous, current or next line add them to total part_num_sum
        all_symbol_ids = list(set(previous_symbols + current_symbols + next_symbols))

        for digit_id in current_digits:
            if digit_id in seen_ids:
                continue
            print(f"all digits: {current_digits}")
            print(f"current digit: {digit_id}: {current_line[digit_id]}")
            for id in all_symbol_ids:
                print(f"all ids: {all_symbol_ids}")
                ids = [id-1, id, id+1]
                print(f"current ids: {ids}")
                for id in ids:
                    if digit_id == id:
                        # if current element is adjacent to a symbol, look ahead and behind to get full number:
                        behind_done = False
                        ahead_done = False
                        id_start = digit_id
                        id_end = digit_id
                        # look ahead:
                        while not ahead_done:
                            if (id_end+1) in current_digits:
                                id_end += 1
                            else:
                                ahead_done = True
                        # look behind:
                        while not behind_done:
                            if (id_start-1) in current_digits:
                                id_start -= 1
                            else:
                                behind_done = True

                        captured_value = int(current_line[id_start:id_end+1])
                        print(captured_value)
                        part_num_sum += captured_value
                        for seen_id in range(id_start, id_end+1):
                            seen_ids.append(seen_id)

        previous_line = current_line
    print(f"Sum Part One: {part_num_sum}")


def get_symbol_ids(line):
    symbol_idx = []
    for _idx, char in enumerate(line):
        if not char == '.' and not char.isdigit():
            symbol_idx.append(_idx)
    return symbol_idx


def get_digit_ids(line):
    digit_idx = []
    for _idx, char in enumerate(line):
        if char.isdigit():
            digit_idx.append(_idx)
    return digit_idx


def get_full_number(line, digit_ids, start_id):
    # get start of number:
    behind_done = False
    id_start = start_id
    while not behind_done:
        if (id_start-1) in digit_ids:
            id_start -= 1
        else:
            behind_done = True
    # get end of number:
    ahead_done = False
    id_end = start_id
    while not ahead_done:
        if (id_end+1) in digit_ids:
            id_end += 1
        else:
            ahead_done = True
    return line[id_start:id_end+1]


def part_two(lines):
    gear_ratio_sum = 0

    lines_count = len(lines)

    previous_line = ''

    previous_symbols = []
    current_symbols = []
    next_symbols = []

    current_digits = []

    for i in range(lines_count):
        line_sum = 0
        print(f"Line {i}")

        current_line = lines[i]
        next_line = lines[i+1] if i+1 < lines_count else ''

        current_symbols = get_symbol_ids(current_line)

        previous_digits = get_digit_ids(previous_line)
        current_digits = get_digit_ids(current_line)
        next_digits = get_digit_ids(next_line)

        for symbol_id in current_symbols:
            first_num = 0
            second_num = 0
            # check if symbol is adjacent to two numbers on current line: ex: ...123*567...
            if symbol_id-1 in current_digits and symbol_id+1 in current_digits:
                print(f'{i}: current line does match')
                # get first number:
                behind_done = False
                id_start = symbol_id
                while not behind_done:
                    if (id_start-1) in current_digits:
                        id_start -= 1
                    else:
                        behind_done = True
                # get second number:
                ahead_done = False
                id_end = symbol_id
                while not ahead_done:
                    if (id_end+1) in current_digits:
                        id_end += 1
                    else:
                        ahead_done = True

                first_num = current_line[id_start:symbol_id]
                second_num = current_line[symbol_id+1:id_end+1]

            # check if symbol is adjacent to two numbers in previous/next line
            # can only happen if symbol is directly below a '.' and previous/next line has digits in symbol_id-1 and symbol_id+2
            elif previous_line[symbol_id] == '.' and symbol_id-1 in previous_digits and symbol_id+1 in previous_digits:
                print('previous_line could match')
                # get first number:
                behind_done = False
                id_start = symbol_id
                while not behind_done:
                    if (id_start-1) in previous_digits:
                        id_start -= 1
                    else:
                        behind_done = True
                # get second number:
                ahead_done = False
                id_end = symbol_id
                while not ahead_done:
                    if (id_end+1) in previous_digits:
                        id_end += 1
                    else:
                        ahead_done = True

                first_num = previous_line[id_start:symbol_id]
                second_num = previous_line[symbol_id+1:id_end+1]
            elif next_line[symbol_id] == '.' and symbol_id-1 in next_digits and symbol_id+1 in next_digits:
                print('next_line could match')
                # get first number:
                behind_done = False
                id_start = symbol_id
                while not behind_done:
                    if (id_start-1) in next_digits:
                        id_start -= 1
                    else:
                        behind_done = True
                # get second number:
                ahead_done = False
                id_end = symbol_id
                while not ahead_done:
                    if (id_end+1) in next_digits:
                        id_end += 1
                    else:
                        ahead_done = True

                first_num = next_line[id_start:symbol_id]
                second_num = next_line[symbol_id+1:id_end+1]

            # check if symbol is adjacent to a numbers in previous/next and a number in current line
            elif symbol_id-1 in current_digits or symbol_id+1 in current_digits:
                print("current line matches on one side, check if previous or next line also matches")
                possible_ids = [symbol_id-1, symbol_id, symbol_id+1]
                previous_line_matches = False
                next_line_matches = False
                previous_matched_id = -1
                next_matched_id = -1
                for previous_id in previous_digits:
                    if previous_id in possible_ids:
                        previous_line_matches = True
                        previous_matched_id = previous_id
                for next_id in next_digits:
                    if next_id in possible_ids:
                        next_line_matches = True
                        next_matched_id = next_id

                if symbol_id-1 in current_digits:
                    first_num = get_full_number(current_line, current_digits, symbol_id-1)
                else:
                    first_num = get_full_number(current_line, current_digits, symbol_id+1)

                if previous_line_matches:
                    second_num = get_full_number(previous_line, previous_digits, previous_matched_id)
                if next_line_matches:
                    second_num = get_full_number(next_line, next_digits, next_matched_id)

            # check if symbol is adjacent to a numbers in previous line and a number in next line
            else:
                possible_ids = [symbol_id-1, symbol_id, symbol_id+1]
                previous_line_matches = False
                next_line_matches = False
                previous_matched_id = -1
                next_matched_id = -1
                for previous_id in previous_digits:
                    if previous_id in possible_ids:
                        previous_line_matches = True
                        previous_matched_id = previous_id
                for next_id in next_digits:
                    if next_id in possible_ids:
                        next_line_matches = True
                        next_matched_id = next_id
                if previous_line_matches and next_line_matches:
                    print(f"{i}: matches previous and next")
                    # get number from previous line
                    first_num = get_full_number(previous_line, previous_digits, previous_matched_id)
                    # get number from next line
                    second_num = get_full_number(next_line, next_digits, next_matched_id)

            print(f"{first_num}*{second_num}")
            line_sum += int(first_num)*int(second_num)

        previous_line = current_line
        gear_ratio_sum += line_sum
    print(f"Sum Part Two: {gear_ratio_sum}")


with open("day_03/input.txt", "r") as input:
    text = input.read().rstrip()
    lines = text.splitlines()
    # part_one(lines)
    part_two(lines)
