def part_one(lines):
    card_sum = 0
    for line in lines:
        line_sum = 0
        card, all_numbers = line.split(': ')
        card_id = card.split(' ')[1]
        all_winning_numbers, all_scratched_numbers = all_numbers.split(' | ')
        winning_numbers = all_winning_numbers.split(' ')
        scratched_numbers = all_scratched_numbers.split(' ')
        # remove all spaces from lists:
        winning_numbers = [number for number in winning_numbers if number.isdigit()]
        scratched_numbers = [number for number in scratched_numbers if number.isdigit()]
        # check how many scratched numbers are in winning_numbers
        for scratched_number in scratched_numbers:
            if scratched_number in winning_numbers:
                line_sum = line_sum+1 if line_sum == 0 else line_sum*2
        card_sum += line_sum
    print(f"Sum Part One: {card_sum}")


def part_two(lines):
    duplicates = [1 for line in lines]
    for line in lines:
        line_sum = 0
        card, all_numbers = line.split(': ')
        card_id = int(card.split(' ')[-1])
        all_winning_numbers, all_scratched_numbers = all_numbers.split(' | ')
        winning_numbers = all_winning_numbers.split(' ')
        scratched_numbers = all_scratched_numbers.split(' ')
        # remove all spaces from lists:
        winning_numbers = [number for number in winning_numbers if number.isdigit()]
        scratched_numbers = [number for number in scratched_numbers if number.isdigit()]
        # check how many scratched numbers are in winning_numbers
        for scratched_number in scratched_numbers:
            if scratched_number in winning_numbers:
                line_sum = line_sum+1
        # for each instance of the current card (duplicates[card_id-1]):
        # add duplicates for the next n cards, where n is the amount of matching numbers on one of the current cards (they are identical)
        for i in range(line_sum):
            duplicates[card_id+i] += 1*duplicates[card_id-1]
        card_amount = sum(duplicates)
    print(f"Sum Part Two: {card_amount}")


with open("day_04/input.txt", "r") as input:
    text = input.read().rstrip()
    lines = text.splitlines()
    part_one(lines)
    part_two(lines)
