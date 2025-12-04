import time

# Indication of files
puzzle_input = "Input/day04.txt"
test_input = "Input/day04_short.txt"

def parse_input(filename):
    with open(filename) as inp:
            lines = [list(line.strip()) for line in inp.readlines()]
    return lines

def find_paper_rolls(grid):
    paper_rolls_loc = set()
    for y, row in enumerate(grid):
        for x, space in enumerate(row):
            if space == '@':
                paper_rolls_loc.add((x, y))
    return paper_rolls_loc

def find_bounds(grid):
    return len(grid[0]), len(grid)

def is_roll(paper_loc_set, roll, neighbour_direction):
    return (neighbour_direction[0] + roll[0] , neighbour_direction[1] + roll[1]) in paper_loc_set

def find_neighbours(paper_loc_set, neighbour_directions):
    num_neighbours = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set()}
    for roll in paper_loc_set:
        count_neighbours = 0
        for direction in neighbour_directions:
            count_neighbours += 1 if is_roll(paper_loc_set, roll, direction) else 0
        current_set = num_neighbours[count_neighbours]
        current_set.add(roll)
        num_neighbours[count_neighbours] = current_set
    return num_neighbours

def remove_rolls(paper_loc_set, num_neighbours, max_neighbours):
    for x in range(0, max_neighbours):
        for loc in num_neighbours[x]:
            paper_loc_set.remove(loc)
    return paper_loc_set

def calc_accessible_rolls(num_neighbours, max_neighbours):
    return sum([len(num_neighbours[x]) for x in range(0, max_neighbours)])

def main(filename, max_neighbours):
    start_time = time.time_ns()
    version = "test input" if filename.find("short") > -1 else "puzzle input"

    # parse input
    grid = parse_input(filename)

    # starting var
    neighbour_directions = [(0, 1), (0, - 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
    accessible_rolls = 0

    paper_loc_set = find_paper_rolls(grid)
    num_neighbours = find_neighbours(paper_loc_set, neighbour_directions)

    # deel 1
    accessible_rolls += calc_accessible_rolls(num_neighbours, max_neighbours)
    print(f"{version}:\npart 1: {accessible_rolls}")

    # deel 2
    while sum([len(num_neighbours[x]) for x in range(0, max_neighbours)]) != 0:
         paper_loc_set = remove_rolls(paper_loc_set, num_neighbours, max_neighbours)
         num_neighbours = find_neighbours(paper_loc_set, neighbour_directions)
         accessible_rolls += calc_accessible_rolls(num_neighbours, max_neighbours)

    print(f"{version}:\npart 2: {accessible_rolls}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

main(test_input, 4)
main(puzzle_input, 4)