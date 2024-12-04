def part1(grid, word):
    def check_direction(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (1, 0),   # Down
        (0, 1),   # Right
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 0),  # Up
        (0, -1),  # Left
        (-1, -1), # Diagonal up-left
        (-1, 1)   # Diagonal up-right
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1
    return count


def part2(grid):
    def is_valid_xmas(x, y):
        """
        Check if the cell (x, y) is the center of an X-MAS pattern.
        """
        try:
            mas1 = (
                grid[x - 1][y - 1] == "M" and
                grid[x][y] == "A" and
                grid[x + 1][y + 1] == "S"
            )
            sam1 = (
                grid[x - 1][y - 1] == "S" and
                grid[x][y] == "A" and
                grid[x + 1][y + 1] == "M"
            )
            # Diagonal 2 (Top-right to bottom-left)
            mas2 = (
                grid[x - 1][y + 1] == "M" and
                grid[x][y] == "A" and
                grid[x + 1][y - 1] == "S"
            )
            sam2 = (
                grid[x - 1][y + 1] == "S" and
                grid[x][y] == "A" and
                grid[x + 1][y - 1] == "M"
            )

            return (mas1 or sam1) and (mas2 or sam2)
        except IndexError:
            return False

    count = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if is_valid_xmas(x, y):
                count += 1
    return count


def read_input(file_name):
    with open(file_name, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

grid = read_input('input.txt')

grid_list = [list(row) for row in grid]

word = "XMAS"

part1_res = part1(grid_list, word)
part2_res = part2(grid)

print(f'Part 1 answer: {part1_res}')
print(f'Part 2 answer: {part2_res}')

