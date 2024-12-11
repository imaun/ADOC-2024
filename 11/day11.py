from collections import Counter


def split_number(n):
    s = str(n)
    mid = len(s) // 2
    return int(s[:mid]), int(s[mid:])


def blink(stones, total_blinks):
    stone_counts = Counter(stones)

    for _ in range(total_blinks):
        new_stone_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                left, right = split_number(stone)
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                new_stone_counts[stone * 2024] += count

        stone_counts = new_stone_counts

    return sum(stone_counts.values())


# Input
initial_stones = [92, 0, 286041, 8034, 34394, 795, 8, 2051489]

# Part 1: 25 blinks
part1_result = blink(initial_stones, 25)
print(part1_result)

part2_result = blink(initial_stones, 75)
print(part2_result)