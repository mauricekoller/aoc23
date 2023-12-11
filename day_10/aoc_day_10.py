def part_one(text):
    # X-Axis: Char along the line
    # Y-Axis: Line Number
    lines = text.split('\n')
    max_x = len(lines[0])
    max_y = len(lines)
    for line_idx, line in enumerate(lines):
        for char_idx, char in enumerate(line):
            if char == 'S':
                starting_x = char_idx
                starting_y = line_idx
    print(starting_x, starting_y)
    # Check all surrounding tiles:
    # Check if above are any of:    |,7,F
    # Check if below are any of:    |,L,J
    # Check if left are any of:     -,L,F
    # Check if right are any of:    -,J,7
    # . is always the Ground

    if lines[starting_y-1][starting_x] in ['|', '7', 'F']:
        current_x = starting_x
        current_y = starting_y-1
    elif lines[starting_y+1][starting_x] in ['|', 'L', 'J']:
        current_x = starting_x
        current_y = starting_y+1
    elif lines[starting_y][starting_x-1] in ['-', 'L', 'F']:
        current_x = starting_x - 1
        current_y = starting_y
    elif lines[starting_y][starting_x+1] in ['-', 'J', '7']:
        current_x = starting_x + 1
        current_y = starting_y
    else:
        print("No adjacent matching Symbol found for S")

    last_x = starting_x
    last_y = starting_y

    print(current_x, current_y)
    # Keep track of where we came from, check where our symbol can go to and move there
    current_symbol = lines[current_y][current_x]
    print(current_symbol)
    max_distance = 1
    while current_symbol != 'S':
        if current_symbol == '|':
            if last_y < current_y:  # move down
                last_y = current_y
                current_y += 1
                last_x = current_x
            else:  # move up
                last_y = current_y
                current_y -= 1
                last_x = current_x
        elif current_symbol == '-':
            if last_x < current_x:  # move right
                last_x = current_x
                current_x += 1
                last_y = current_y
            else:  # move left
                last_x = current_x
                current_x -= 1
                last_y = current_y
        elif current_symbol == 'L':
            if last_y < current_y:  # move right
                last_x = current_x
                current_x += 1
                last_y = current_y
            else:  # move up
                last_y = current_y
                current_y -= 1
                last_x = current_x
        elif current_symbol == 'J':
            if last_y < current_y:  # move left
                last_x = current_x
                current_x -= 1
                last_y = current_y
            else:  # move up
                last_y = current_y
                current_y -= 1
                last_x = current_x
        elif current_symbol == 'F':
            if last_y > current_y:  # move right
                last_x = current_x
                current_x += 1
                last_y = current_y
            else:  # move down
                last_y = current_y
                current_y += 1
                last_x = current_x
        elif current_symbol == '7':
            if last_y > current_y:  # move left
                last_x = current_x
                current_x -= 1
                last_y = current_y
            else:  # move down
                last_y = current_y
                current_y += 1
                last_x = current_x
        else:
            print(f"Couldn't match any Symbol at position {current_x, current_y}")
        current_symbol = lines[current_y][current_x]
        max_distance += 1
        print(current_symbol)
    print(f"Sum Part One: {max_distance/2}")


def part_two(text):
    # X-Axis: Char along the line
    # Y-Axis: Line Number
    lines = text.split('\n')
    max_x = len(lines[0])
    max_y = len(lines)
    loop = []

    for line_idx, line in enumerate(lines):
        for char_idx, char in enumerate(line):
            if char == 'S':
                starting_x = char_idx
                starting_y = line_idx
    print(starting_x, starting_y)
    loop.append([starting_x, starting_y])
    # Check all surrounding tiles:
    # Check if above are any of:    |,7,F
    # Check if below are any of:    |,L,J
    # Check if left are any of:     -,L,F
    # Check if right are any of:    -,J,7
    # . is always the Ground

    if lines[starting_y-1][starting_x] in ['|', '7', 'F']:
        current_x = starting_x
        current_y = starting_y-1
    elif lines[starting_y+1][starting_x] in ['|', 'L', 'J']:
        current_x = starting_x
        current_y = starting_y+1
    elif lines[starting_y][starting_x-1] in ['-', 'L', 'F']:
        current_x = starting_x - 1
        current_y = starting_y
    elif lines[starting_y][starting_x+1] in ['-', 'J', '7']:
        current_x = starting_x + 1
        current_y = starting_y
    else:
        print("No adjacent matching Symbol found for S")
    loop.append([current_x, current_y])

    last_x = starting_x
    last_y = starting_y

    print(current_x, current_y)
    # Keep track of where we came from, check where our symbol can go to and move there
    current_symbol = lines[current_y][current_x]
    print(current_symbol)
    max_distance = 1
    while current_symbol != 'S':
        if current_symbol == '|':
            if last_y < current_y:  # move down
                last_y = current_y
                current_y += 1
                last_x = current_x
            else:  # move up
                last_y = current_y
                current_y -= 1
                last_x = current_x
        elif current_symbol == '-':
            if last_x < current_x:  # move right
                last_x = current_x
                current_x += 1
                last_y = current_y
            else:  # move left
                last_x = current_x
                current_x -= 1
                last_y = current_y
        elif current_symbol == 'L':
            if last_y < current_y:  # move right
                last_x = current_x
                current_x += 1
                last_y = current_y
            else:  # move up
                last_y = current_y
                current_y -= 1
                last_x = current_x
        elif current_symbol == 'J':
            if last_y < current_y:  # move left
                last_x = current_x
                current_x -= 1
                last_y = current_y
            else:  # move up
                last_y = current_y
                current_y -= 1
                last_x = current_x
        elif current_symbol == 'F':
            if last_y > current_y:  # move right
                last_x = current_x
                current_x += 1
                last_y = current_y
            else:  # move down
                last_y = current_y
                current_y += 1
                last_x = current_x
        elif current_symbol == '7':
            if last_y > current_y:  # move left
                last_x = current_x
                current_x -= 1
                last_y = current_y
            else:  # move down
                last_y = current_y
                current_y += 1
                last_x = current_x
        else:
            print(f"Couldn't match any Symbol at position {current_x, current_y}")
        current_symbol = lines[current_y][current_x]
        max_distance += 1
        loop.append([current_x, current_y])
        print(current_symbol)

    # remove all pipes that are not part of the loop with a 0
    new_lines = []
    for line_idx, line in enumerate(lines):
        new_line = []
        for char_idx, char in enumerate(line):
            if [char_idx, line_idx] not in loop and char != '.':
                new_line.append(0)
            else:
                new_line.append(char)
        new_lines.append(new_line)
    for line in new_lines:
        print(''.join([str(char) for char in line]))


with open("day_10/input.txt", "r") as input:
    text = input.read().rstrip()
    # lines = text.splitlines()
    part_one(text)
    part_two(text)
