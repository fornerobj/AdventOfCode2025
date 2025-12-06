import math

with open("input", "r") as f:
    data = f.read().strip().splitlines()

ops = data[-1].split()
nums = [list(map(int, line.split())) for line in data[:-1]]

n, m = len(nums), len(nums[0])

pt1 = 0
for col, op in zip(zip(*nums), ops):
    if op == '+':
        pt1 += sum(col)
    else:
        pt1 += math.prod(col)

pt2 = 0
current_nums = []
height = len(data) - 1
width  = len(data[0])
for col in reversed(range(width)):
    # Build the number in this column
    digits = [data[row][col] for row in range(height) if data[row][col].isdigit()]
    if digits:
        current_nums.append(int("".join(digits)))

    # If this column has an operator, evaluate & reset
    if col < len(data[-1]) and data[-1][col] in "+*":
        if data[-1][col] == '+':
            pt2 += sum(current_nums)
        else:
            pt2 += math.prod(current_nums)
        current_nums.clear()

print("Part 1:", pt1)
print("Part 2:", pt2)


