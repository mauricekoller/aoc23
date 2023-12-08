def matches_joker(input_str):
    # we need to keep track of how many jokers we have and how many we have used for the two edge cases FullHouse and TwoPair:
    # AAJK3 is NOT a Fullhouse but will get treated as one currently, since we get: [['A',3]['K',2]['3',2]]
    # as long as there is a Joker everything is automatically a Pair and we currently don't check if the Joker has been used already
    seen_chars = []
    matches = []
    joker_counter = 0
    for char in input_str:
        if char == 'J':
            joker_counter += 1
    for search_char in input_str:
        jokers_used = 0
        char_counter = 0
        if search_char not in seen_chars:
            seen_chars.append(search_char)
        else:
            continue

        for current_char in input_str:
            if current_char == search_char or current_char == 'J':
                char_counter += 1
                if current_char == 'J':
                    jokers_used += 1
        matches.append([search_char, char_counter, jokers_used])
    # sort dict by values desc
    matches = sorted(matches, key=lambda x: x[1], reverse=True)
    return matches, joker_counter


def matches(input_str):
    seen_chars = []
    matches = []
    for search_char in input_str:
        char_counter = 0
        if search_char not in seen_chars:
            seen_chars.append(search_char)
        else:
            continue

        for current_char in input_str:
            if current_char == search_char:
                char_counter += 1
        matches.append([search_char, char_counter])
    # sort dict by values desc
    matches = sorted(matches, key=lambda x: x[1], reverse=True)
    return matches


def poker_sort_key(item):
    sorting_order = '23456789TJQKA'
    return [sorting_order.index(char) if char in sorting_order else char for char in item[0]]


def poker_sort_key_joker(item):
    sorting_order = 'J23456789TQKA'
    return [sorting_order.index(char) if char in sorting_order else char for char in item[0]]


def part_one(lines):
    general_ranks = [[]for _ in range(7)]
    for line in lines:
        hand = {}
        cards, bid = line.split()
        print(cards, bid)
        hand['cards'] = cards
        hand['bid'] = bid
        # Check the rank of the hand:
        # 0: high card
        # 1: pair
        # 2: 2 pair
        # 3: 3 of a kind
        # 4: fullhouse
        # 5: 4 of a kind
        # 6: 5 of a kind
        matched_str = matches(cards)
        max_val = matched_str[0][1]
        if max_val == 5:
            rank = 6
        elif max_val == 4:
            rank = 5
        elif max_val == 3:
            if matched_str[1][1] == 2:
                rank = 4
            else:
                rank = 3
        elif max_val == 2:
            if matched_str[1][1] == 2:
                rank = 2
            else:
                rank = 1
        else:
            rank = 0
        print(rank)
        general_ranks[rank].append([cards, bid])

    # sort each general_rank internally comparing first, second, ... card
    sorted_ranks = []
    for general_rank in general_ranks:
        if len(general_rank) > 0:
            sorted_rank = sorted(general_rank, key=poker_sort_key)
            for _sorted_rank in sorted_rank:
                sorted_ranks.append(_sorted_rank)

    print(sorted_ranks)

    sum = 0
    for i, hand in enumerate(sorted_ranks):
        sum += (i+1)*int(hand[1])

    print(f"Sum Part One: {sum}")


def part_two(lines):
    general_ranks = [[]for _ in range(7)]
    for line in lines:
        hand = {}
        cards, bid = line.split()
        print(cards, bid)
        hand['cards'] = cards
        hand['bid'] = bid
        # Check the rank of the hand:
        # 0: high card
        # 1: pair
        # 2: 2 pair
        # 3: 3 of a kind
        # 4: fullhouse
        # 5: 4 of a kind
        # 6: 5 of a kind
        matched_str, jokers_found = matches_joker(cards)
        max_val = matched_str[0][1]
        jokers_used = matched_str[0][2]
        jokers_left = jokers_found - jokers_used
        if max_val == 5:
            rank = 6
        elif max_val == 4:
            rank = 5
        elif max_val == 3:
            if (matched_str[1][1] == 2 and matched_str[1][2] <= jokers_left) or (matched_str[1][1] == 3 and matched_str[1][2] <= jokers_left+1):
                rank = 4
            else:
                rank = 3
        elif max_val == 2:
            if matched_str[1][1] == 2 and matched_str[1][2] <= jokers_left:
                rank = 2
            else:
                rank = 1
        else:
            rank = 0
        # print(rank)
        general_ranks[rank].append([cards, bid])

    # sort each general_rank internally comparing first, second, ... card
    sorted_ranks = []
    for general_rank in general_ranks:
        if len(general_rank) > 0:
            sorted_rank = sorted(general_rank, key=poker_sort_key_joker)
            for _sorted_rank in sorted_rank:
                sorted_ranks.append(_sorted_rank)

    for line in sorted_ranks:
        print(line)

    sum = 0
    for i, hand in enumerate(sorted_ranks):
        sum += (i+1)*int(hand[1])

    print(f"Sum Part Two: {sum}")


with open("day_07/input.txt", "r") as input:
    text = input.read().rstrip()
    lines = text.splitlines()
    part_one(lines)
    part_two(lines)
