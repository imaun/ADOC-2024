def parse_map(puzzle_input):
    antennas = []
    for y, row in enumerate(puzzle_input):
        for x, cell in enumerate(row):
            if cell != '.':
                antennas.append((cell, x, y))
    return antennas

def find_antinodes(antennas, width, height):
    antinodes = set()

    for i, (freq1, x1, y1) in enumerate(antennas):
        for freq2, x2, y2 in antennas[i+1:]:
            if freq1 != freq2:
                continue

            dx, dy = x2 - x1, y2 - y1

            # Check for valid antinodes
            ax1, ay1 = x1 - dx, y1 - dy
            ax2, ay2 = x2 + dx, y2 + dy

            # Add the first antinode if it lies within bounds
            if 0 <= ax1 < width and 0 <= ay1 < height:
                antinodes.add((ax1, ay1))

            # Add the second antinode if it lies within bounds
            if 0 <= ax2 < width and 0 <= ay2 < height:
                antinodes.add((ax2, ay2))

    # Include antennas themselves as antinodes when valid
    for freq, x, y in antennas:
        valid_as_antinode = any(
            freq == freq2 and (
                (2 * x - x2, 2 * y - y2) == (x1, y1) or
                (x2, y2) == (2 * x - x1, 2 * y - y1)
            )
            for freq2, x2, y2 in antennas if freq == freq2
        )
        if valid_as_antinode:
            antinodes.add((x, y))

    return antinodes

def part1(puzzle_input):
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    antennas = parse_map(puzzle_input)
    antinodes = find_antinodes(antennas, width, height)
    return len(antinodes)

def read_input(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]


example = read_input('input.txt')

print(example)

print(part1(example))

