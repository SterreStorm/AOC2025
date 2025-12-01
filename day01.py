
def parse_input(filename):
    rotations = []
    with open(filename, "r") as inp:
        for line in inp.readlines():
            rotations.append(line.strip())
    return rotations

def rotate(filename, starting_pos):
    count = 0
    current_pos = starting_pos
    rotations = parse_input(filename)
    for rotation in rotations:
        previous_pos = current_pos
        direction = rotation[0:1]
        movement = int(rotation[1:])

        # Add full rotations to count, determine non-full rotation
        count += int(movement/100)
        movement = movement % 100

        current_pos = (previous_pos - movement) if direction == "L" else previous_pos + movement

        # "L" movement past 0
        if current_pos < 0 and previous_pos != 0:
            count += 1
            current_pos += 100

        # "R" Movement past 0
        if previous_pos < 100 < current_pos:
            count += 1

        # Current position on the dial
        current_pos = current_pos % 100

        # 0?
        if current_pos == 0:
            count += 1

    print(f"password: {count}")


rotate("Input/day01_short.txt", 50)
rotate("Input/day01.txt", 50)