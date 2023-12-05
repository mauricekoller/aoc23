def create_map_list(paragraph):
    return_list = []
    for line in paragraph:
        dest_start, source_start, range_len = line.split()
        return_list.append([int(source_start), int(dest_start), int(range_len)])
    return return_list


def find_in_list(list, val):
    for list in list:
        dest_start = list[0]
        dest_end = dest_start+list[2]-1
        if dest_start <= val <= dest_end:
            return list[1]+(val-dest_start)
    return val


def find_in_list_reverse(list, val):
    for list in list:
        source_start = list[1]
        dest_end = source_start+list[2]-1
        if source_start <= val <= dest_end:
            return list[0]+(val-source_start)
    return val


def part_one(text):
    paragraphs = text.split('\n\n')
    # get all seeds into list
    seeds = [int(val) for val in paragraphs[0].split(': ')[1].split()]

    # create dicts from each line of mappings
    seed_to_soil_map = create_map_list(paragraphs[1].split('\n')[1:])
    soil_to_fertilizer_map = create_map_list(paragraphs[2].split('\n')[1:])
    fertilizer_to_water_map = create_map_list(paragraphs[3].split('\n')[1:])
    water_to_light_map = create_map_list(paragraphs[4].split('\n')[1:])
    light_to_temperature_map = create_map_list(paragraphs[5].split('\n')[1:])
    temperature_to_humidty_map = create_map_list(paragraphs[6].split('\n')[1:])
    humidity_to_location_map = create_map_list(paragraphs[7].split('\n')[1:])

    # iterate over all seeds and find lowest location number
    smallest_location = float('inf')
    for seed in seeds:
        # print(seed)
        soil = find_in_list(seed_to_soil_map, seed)
        # print(soil)
        fertilizer = find_in_list(soil_to_fertilizer_map, soil)
        # print(fertilizer)
        water = find_in_list(fertilizer_to_water_map, fertilizer)
        # print(water)
        light = find_in_list(water_to_light_map, water)
        # print(light)
        temperature = find_in_list(light_to_temperature_map, light)
        # print(temperature)
        humidity = find_in_list(temperature_to_humidty_map, temperature)
        # print(humidity)
        location = find_in_list(humidity_to_location_map, humidity)
        # print(location)
        # print('')
        smallest_location = min(smallest_location, location)

    print(f"Part One: Nearest Location: {smallest_location}")


def part_two(text):
    paragraphs = text.split('\n\n')
    # get all seeds into list
    seeds = [int(val) for val in paragraphs[0].split(': ')[1].split()]
    seeds = [seeds[i:i+2]for i in range(0, len(seeds), 2)]

    # create dicts from each line of mappings
    seed_to_soil_map = create_map_list(paragraphs[1].split('\n')[1:])
    soil_to_fertilizer_map = create_map_list(paragraphs[2].split('\n')[1:])
    fertilizer_to_water_map = create_map_list(paragraphs[3].split('\n')[1:])
    water_to_light_map = create_map_list(paragraphs[4].split('\n')[1:])
    light_to_temperature_map = create_map_list(paragraphs[5].split('\n')[1:])
    temperature_to_humidty_map = create_map_list(paragraphs[6].split('\n')[1:])
    humidity_to_location_map = create_map_list(paragraphs[7].split('\n')[1:])

    # search backwards:
    for location in range(100000000):
        humidity = find_in_list_reverse(humidity_to_location_map, location)
        temperature = find_in_list_reverse(temperature_to_humidty_map, humidity)
        light = find_in_list_reverse(light_to_temperature_map, temperature)
        water = find_in_list_reverse(water_to_light_map, light)
        fertilizer = find_in_list_reverse(fertilizer_to_water_map, water)
        soil = find_in_list_reverse(soil_to_fertilizer_map, fertilizer)
        seed = find_in_list_reverse(seed_to_soil_map, soil)
        # check if seed exists:
        for _seed in seeds:
            if _seed[0] <= seed < (_seed[0]+_seed[1]):
                print(f"Part Two: Nearest Location: {location} for seed {seed}")
                return


with open("day_05/input.txt", "r") as input:
    text = input.read().rstrip()
    # lines = text.splitlines()
    # part_one(text)
    part_two(text)
