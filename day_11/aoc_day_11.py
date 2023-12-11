def part_one(text):
    new_text = []
    # find all rows that contain no '#' and expand them
    for row in text.splitlines():
        if all(char == '.' for char in row):
            new_text.append([char for char in row])
        new_text.append([char for char in row])

    # find all columsn that contain no '#' and expand them
    lines_to_duplicate = []
    for i in range(len(new_text[0])):
        if all(line[i] == '.' for line in new_text):
            lines_to_duplicate.append(i)
    offset = 0
    for i in lines_to_duplicate:
        for idx, row in enumerate(new_text):
            new_row = []
            for c_idx, char in enumerate(row):
                if c_idx == i+offset:
                    new_row.append(char)
                new_row.append(char)
            new_text[idx] = new_row
        offset += 1

    for row in new_text:
        print(''.join(row))

    # make list off all #s we have to check:
    vertices = []
    for row_idx, row in enumerate(new_text):
        for char_idx, char in enumerate(row):
            if char == '#':
                vertices.append([row_idx, char_idx])

    # moving diagonally makes no sense at all so just move horizontally and vertically:
    total_min_distances = 0
    for index, vertice1 in enumerate(vertices):
        for vertice2 in vertices[index:]:
            min_distance = sum([abs(v2-v1) for v1, v2 in zip(vertice1, vertice2)])
            total_min_distances += min_distance

    print(f"Total Min Distance: {total_min_distances}")


def part_two(text):
    lines = text.splitlines()
    rows_to_expand = []
    # find all rows that contain no '#' and expand them
    for row_idx, row in enumerate(lines):
        if all(char == '.' for char in row):
            rows_to_expand.append(row_idx)

    # find all collumns that contain no '#' and expand them
    cols_to_expand = []
    for i in range(len(lines[0])):
        if all(line[i] == '.' for line in lines):
            cols_to_expand.append(i)

    # make list off all #s we have to check:
    vertices = []
    for row_idx, row in enumerate(lines):
        for char_idx, char in enumerate(row):
            if char == '#':
                vertices.append([row_idx, char_idx])

    # moving diagonally makes no sense at all so just move horizontally and vertically:
    total_min_distances = 0
    for index, vertice1 in enumerate(vertices):
        for vertice2 in vertices[index:]:
            rows = sorted([vertice1[0], vertice2[0]])
            cols = sorted([vertice1[1], vertice2[1]])
            extra_rows = (1000000-1) * sum([1 if (idx in range(rows[0], rows[1]+1)) else 0 for idx in rows_to_expand])
            extra_columns = (1000000-1) * sum([1 if (idx in range(cols[0], cols[1]+1)) else 0 for idx in cols_to_expand])
            vertical_dist = abs(vertice1[0]-vertice2[0])+extra_rows
            horizontal_dist = abs(vertice1[1]-vertice2[1])+extra_columns
            min_distance = sum([abs(v2-v1)+extra for v1, v2, extra in zip(vertice1, vertice2, [extra_rows, extra_columns])])
            total_min_distances += min_distance

    print(f"Total Min Distance: {total_min_distances}")


with open("day_11/input.txt", "r") as input:
    text = input.read().rstrip()
    # lines = text.splitlines()
    part_one(text)
    part_two(text)
