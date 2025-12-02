
puzzle_input = "Input/day02.txt"
test_input = "Input/day02_short.txt"

def parse_input(filename):
    with open(filename) as inp:
        ranges = [(int(x[0]), int(x[1])) for x in [y.split("-") for y in inp.readline().strip().split(',')]]
    return ranges

def find_invalid(pair):
    current_id, end_range = pair
    invalid_ids = []
    invalid_ids_pt2 = []
    for current_id  in range(current_id, end_range + 1):
        str_id = str(current_id)
        len_id = len(str_id)
    # part one
        if len_id % 2 == 0:
            half = len_id // 2
            if int(str_id[0:half]) == int(str_id[half:]):
                invalid_ids.append(current_id)

    # part two
        i = (str_id + str_id).find(str_id, 1, -1)
        if i > -1 and current_id not in invalid_ids:
            invalid_ids_pt2.append(current_id)
    return invalid_ids, invalid_ids_pt2

def main(filename):
    dataset = "Puzzle input" if filename.find("short") == -1 else "Test input"
    sum_pairs_pt1 = 0
    sum_pairs_pt2 = 0
    ranges = parse_input(filename)
    for pair in ranges:
        pt_1, pt_2 = find_invalid(pair)
        sum_pairs_pt1 += sum(pt_1)
        sum_pairs_pt2 += sum(pt_1) + sum(pt_2)

    print(f"{dataset}:\n Part 1: {sum_pairs_pt1} \n Part 2: {sum_pairs_pt2}")

main(test_input)
main(puzzle_input)