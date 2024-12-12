def parse_map(map_data):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    grid = []
    start_pos = None
    start_dir = None

    for r, line in enumerate(map_data):
        grid.append(list(line))
        for c, char in enumerate(line):
            if char in directions:
                start_pos = (r, c)
                start_dir = directions[char]
                grid[r][c] = '.'  # Replace the guard symbol with empty space

    return grid, start_pos, start_dir


def turn_right(direction):
    return {(-1, 0): (0, 1),  # Up to Right
            (0, 1): (1, 0),  # Right to Down
            (1, 0): (0, -1),  # Down to Left
            (0, -1): (-1, 0)}[direction]  # Left to Up


def simulate_guard(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    position = start_pos
    direction = start_dir

    while True:
        visited.add(position)
        next_row, next_col = position[0] + direction[0], position[1] + direction[1]

        if not (0 <= next_row < rows and 0 <= next_col < cols):
            break

        if grid[next_row][next_col] == '#':
            direction = turn_right(direction)  # Turn right
        else:
            position = (next_row, next_col)  # Move forward

    return visited


def detect_loop(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    seen = set()
    position = start_pos
    direction = start_dir

    while True:
        state = (position, direction)
        if state in seen:  # Loop detected
            return True
        seen.add(state)

        next_row, next_col = position[0] + direction[0], position[1] + direction[1]

        if not (0 <= next_row < rows and 0 <= next_col < cols):
            return False

        if grid[next_row][next_col] == '#':
            direction = turn_right(direction)  # Turn right
        else:
            position = (next_row, next_col)  # Move forward


def part1(map_data):
    grid, start_pos, start_dir = parse_map(map_data)
    visited = simulate_guard(grid, start_pos, start_dir)
    return len(visited)


def part2(map_data):
    grid, start_pos, start_dir = parse_map(map_data)
    rows, cols = len(grid), len(grid[0])
    loop_positions = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) != start_pos and grid[r][c] == '.':  # empty positions
                # temporary obstruction
                grid[r][c] = '#'
                if detect_loop(grid, start_pos, start_dir):
                    loop_positions += 1
                # Remove the obstruction
                grid[r][c] = '.'

    return loop_positions


def read_input(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]


input_data = read_input('input.txt')
part1_res = part1(input_data)
part2_res = part2(input_data)

print(f"Part 1: {part1_res}")
print(f"Part 2: {part2_res}")
