def parse_input(input_data):
    sections = input_data.strip().split("\n\n")
    ordering_rules = sections[0].splitlines()
    updates = [list(map(int, update.split(','))) for update in sections[1].splitlines()]

    rules = []
    for rule in ordering_rules:
        x, y = map(int, rule.split('|'))
        rules.append((x, y))

    return rules, updates


def is_correct_order(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def find_middle_page(update):
    middle_index = len(update) // 2
    return update[middle_index]


def solve(input_data):
    rules, updates = parse_input(input_data)
    middle_sum = 0

    for update in updates:
        if is_correct_order(update, rules):
            middle_sum += find_middle_page(update)

    return middle_sum

def solve_2(data):
    rules, updates = parse_input(data)
    total_middle_sum = 0

    def fix_order(update, rules):
        sorted_update = sorted(update, key=lambda page: sum(page == rule[1] for rule in rules if rule[0] in update))
        return sorted_update

    for update in updates:
        if not is_correct_order(update, rules):
            corrected_update = fix_order(update, rules)
            total_middle_sum += find_middle_page(corrected_update)

    return total_middle_sum

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read()

input_data = read_input('input.txt')
result_1 = solve(input_data)
result_2 = solve_2(input_data)

print(f"Part1: {result_1}")
print(f'Part2: {result_2}')
