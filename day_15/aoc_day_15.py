from functools import cache


@cache
def determine_hash(text):
    sequence_res = 0
    for char in text:
        ascii_val = ord(char)
        sequence_res += ascii_val
        sequence_res *= 17
        sequence_res %= 256
    return sequence_res


def part_one(text):
    total_sum = 0
    for sequence in text.split(','):
        sequence_res = determine_hash(sequence)
        total_sum += sequence_res
    print(f"Result Part 1: {total_sum}")


def part_two(text):
    total_sum = 0
    # boxes will look like this:
    # [[ [[label,focal_length]] [[label,focal_length]] ] [ [ [label, focal_length] ] ]]
    boxes = [[] for _ in range(256)]
    for sequence in text.split(','):
        if '=' in sequence:
            label, focal_length = sequence.split('=')
            box = determine_hash(label)
            # check if label already exists:
            if label in [label for label, _focal_length in boxes[box]]:
                idx = [label for label, _focal_length in boxes[box]].index(label)
                boxes[box][idx][1] = focal_length
            else:
                # append to box
                boxes[box].append([label, focal_length])
        else:
            label = sequence.split('-')[0]
            box = determine_hash(label)
            if label in [label for label, _focal_length in boxes[box]]:
                idx = [label for label, _focal_length in boxes[box]].index(label)
                boxes[box].pop(idx)
    for bix, box in enumerate(boxes):
        box_sum = 0
        for lix, [label, focal_length] in enumerate(box):
            box_sum += (bix+1)*(lix+1)*int(focal_length)
        total_sum += box_sum

    print(f"Result Part 2: {total_sum}")


with open("day_15/input.txt", "r") as input:
    text = input.read().rstrip()
    # lines = text.splitlines()
    part_one(text)
    part_two(text)
