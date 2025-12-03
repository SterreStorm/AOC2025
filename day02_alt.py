import time
from math import log10, ceil, floor

puzzle_input = "Input/day02.txt"
test_input = "Input/day02_short.txt"

def parse_input(filename):
    with open(filename) as inp:
        ranges = [(int(x[0]), int(x[1])) for x in [y.split("-") for y in inp.readline().strip().split(',')]]
    return ranges

def find_segments(len_num):
    segments = [x for x in range(1, (len_num // 2) + 1) if len_num % x == 0]
    segments.reverse()
    return segments

def find_invalids(working_range):
    sum_1 = 0
    sum_2 = 0
    length_num = int(log10(working_range[0]) + 1)
    low, high = working_range
    segments = find_segments(length_num)
    return sum_1, sum_2

def get_ranges(initial_range, exp_start, exp_end):
    working_ranges = []
    start, end = initial_range
    for i in range(exp_start, exp_end + 1):
        if i == exp_start:
            working_ranges.append((start, 10 ** (exp_start + 1) - 1))
        elif i == exp_end:
            working_ranges.append((10 ** i, end))
        else: working_ranges.append((10 ** i, (10 ** 1) - 1))
    return working_ranges

def sum_invalid_range(working_range):
    sum_pt1, sum_pt2 = 0, 0
    pt1, pt2 = find_invalids(working_range)
    sum_pt1 += pt1
    sum_pt2 += pt1 + pt2
    return sum_pt1, sum_pt2

def main(filename):
    #admin
    start_time = time.time_ns()
    dataset = ("Puzzle input" if filename.find("short") == -1 else "Test input")

    # variables
    final_sum_pt1, final_sum_pt2 = 0, 0

    # parse input
    ranges = parse_input(filename)

    for initial_range in ranges:
        exp_start = int(log10(initial_range[0]))
        exp_end = int(log10(initial_range[1]))
        working_ranges = get_ranges(initial_range, exp_start, exp_end) if exp_start != exp_end else [initial_range]
        for working_range in working_ranges:
            print(working_range)
            sum_invalid_range(working_range)
        #     final_sum_pt1 += pt_1
        #     final_sum_pt2 += pt_1 + pt_2

    print(f"{dataset}:\n Part 1: {final_sum_pt1} \n Part 2: {final_sum_pt2}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

main(test_input)