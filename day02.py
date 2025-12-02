import time

puzzle_input = "Input/day02.txt"
test_input = "Input/day02_short.txt"


def parse_input(filename):
    with open(filename) as inp:
        ranges = [(int(x[0]), int(x[1])) for x in [y.split("-") for y in inp.readline().strip().split(',')]]
    return ranges

def check_pt_1(len_id, str_id):
    # part one
    return len_id % 2 == 0 and int(str_id[0:len_id // 2]) == int(str_id[len_id // 2:])

def check_pt_2(str_id):
    i = (str_id + str_id).find(str_id, 1, -1)
    return i > -1

def check_pt2_alt(len_id, str_id):
    divisors = [x for x in range(1, len_id // 2 + 1) if len_id % x == 0]
    for divisor in divisors:
        alt_str = str_id[divisor:] + str_id[:divisor]
        if str_id == alt_str:
            return True
    return False

def sum_invalid(ranges, alt):
    sum_pairs_pt1 = 0
    sum_pairs_pt2 = 0
    for pair in ranges:
        current_id, end_range = pair
        for current_id in range(current_id, end_range + 1):
            str_id = str(current_id)
            len_id = len(str_id)
            if check_pt_1(len_id, str_id):
                sum_pairs_pt1 += current_id
                sum_pairs_pt2 += current_id
            else:
                if check_pt_2(str_id) and not alt: # part two
                    sum_pairs_pt2 += current_id
                elif check_pt2_alt(len_id, str_id): #alternative solution pt 2
                    sum_pairs_pt2 += current_id
    return sum_pairs_pt1, sum_pairs_pt2

def main(filename, alt = False):
    start_time = time.time_ns()
    dataset = ("Puzzle input" if filename.find("short") == -1 else "Test input") + (" (alternatieve uitvoering)" if alt else "")

    ranges = parse_input(filename)
    pt_1, pt_2 = sum_invalid(ranges, alt)


    print(f"{dataset}:\n Part 1: {pt_1} \n Part 2: {pt_2}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

# main(test_input, True)
# main(test_input)
main(puzzle_input, True)