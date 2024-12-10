def parse_map(input_map):
    return [list(map(int, line)) for line in input_map.strip().splitlines()]

def get_neighbors(x, y, rows, cols):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors

def bfs(map_data, start_x, start_y):
    rows, cols = len(map_data), len(map_data[0])
    queue = [(start_x, start_y)]
    visited = set(queue)
    reachable_nines = set()

    while queue:
        x, y = queue.pop(0)
        for nx, ny in get_neighbors(x, y, rows, cols):
            if (nx, ny) not in visited and map_data[nx][ny] == map_data[x][y] + 1:
                visited.add((nx, ny))
                queue.append((nx, ny))
                if map_data[nx][ny] == 9:
                    reachable_nines.add((nx, ny))

    return len(reachable_nines)

def calculate_scores(input_map):
    map_data = parse_map(input_map)
    rows, cols = len(map_data), len(map_data[0])
    total_score = 0

    for x in range(rows):
        for y in range(cols):
            if map_data[x][y] == 0:  # Trailhead
                total_score += bfs(map_data, x, y)

    return total_score

def count_trails(map_data, start_x, start_y):
    rows, cols = len(map_data), len(map_data[0])
    queue = [(start_x, start_y, [(start_x, start_y)])]
    visited_paths = set()
    total_trails = 0

    while queue:
        x, y, path = queue.pop(0)
        for nx, ny in get_neighbors(x, y, rows, cols):
            if map_data[nx][ny] == map_data[x][y] + 1:
                new_path = path + [(nx, ny)]
                path_tuple = tuple(new_path)
                if path_tuple not in visited_paths:
                    visited_paths.add(path_tuple)
                    queue.append((nx, ny, new_path))
                    if map_data[nx][ny] == 9:
                        total_trails += 1

    return total_trails

def calculate_ratings(input_map):
    map_data = parse_map(input_map)
    rows, cols = len(map_data), len(map_data[0])
    total_rating = 0

    for x in range(rows):
        for y in range(cols):
            if map_data[x][y] == 0:  # Trailhead
                total_rating += count_trails(map_data, x, y)

    return total_rating

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read()

input = read_input('input.txt')

print(f'part1: {calculate_scores(input)}')
print(f'part2: {calculate_ratings(input)}')