from itertools import product

def eval_exp(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_form(test_value, numbers, allow_concat=False):
    num_count = len(numbers)
    operators = ['+', '*'] if not allow_concat else ['+', '*', '||']
    operator_comb = product(operators, repeat=num_count - 1)

    for ops in operator_comb:
        if eval_exp(numbers, ops) == test_value:
            return True
    return False

def part1(input_data):
    res = 0

    for line in input_data.strip().split('\n'):
        v, numbers = line.split(':')
        v = int(v.strip())
        numbers = list(map(int, numbers.strip().split()))

        if can_form(v, numbers):
            res += v

    return res

def part2(input_data):
    res = 0

    for line in input_data.strip().split('\n'):
        v, numbers = line.split(':')
        v = int(v.strip())
        numbers = list(map(int, numbers.strip().split()))

        if can_form(v, numbers, allow_concat=True):
            res += v

    return res

def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read()


example = read_input('input.txt')

part1_res = part1(example)
print(part1_res)

part2_res = part2(example)
print(part2_res)