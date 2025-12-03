import time

# Indication of file
puzzle_input = "Input/day03.txt"
test_input = "Input/day03_short.txt"

# Parse input to usable list
def parse_input(filename):
    with open(filename) as inp:
        batteries = [battery.strip() for battery in inp.readlines()]
    return batteries

# find next digit within acceptable range in string
def find_digit(battery, start_loc, end_loc):
    for digit in range(9, 0, -1):
        sDigit = str(digit)
        first_occurence = battery.find(sDigit, start_loc, end_loc)
        if first_occurence != -1:
            return sDigit, (first_occurence + 1)

# finds X amount of digits to find the highest number in a string of numbers
def find_joltage(battery, on_batteries):
    joltage = ""
    start_loc = 0
    for current_on in range(1, on_batteries + 1):
        end_loc = current_on - on_batteries if current_on - on_batteries != 0 else None
        new_digit, position = find_digit(battery, start_loc, end_loc)
        joltage += new_digit
        start_loc = position
    return int(joltage)

# Main function, prints the output of the puzzle
def main(filename):
    start_time = time.time_ns()
    dataset = "puzzle input" if filename.find("short") == -1 else "test input"
    batteries = parse_input(filename)
    sum_joltage_pt1 = sum([find_joltage(battery, 2) for battery in batteries])
    sum_joltage_pt2 = sum([find_joltage(battery, 12) for battery in batteries])

    print(f"Sum joltage ({dataset}): \n deel 1: {sum_joltage_pt1} \n deel 2: {sum_joltage_pt2}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

main(test_input)
main(puzzle_input)