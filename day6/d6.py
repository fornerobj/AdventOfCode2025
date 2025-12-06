import math

with open("input", "r") as f:
    data = f.read().strip().splitlines()
    ops = data[-1].split()
    nums = [data[i].split() for i in range(len(data)-1)]
    nums = [[int(item) for item in sublist] for sublist in nums]

n, m = len(nums), len(nums[0])

pt1 = 0
for pos in range(m):
    subtotal = nums[0][pos]
    for row in range(1,n):
        if ops[pos] == '+':
            subtotal+= nums[row][pos]
        else:
            subtotal *= nums[row][pos]

    pt1 += subtotal
print("Part 1:", pt1)


lines = data
pt2 = 0
vert_nums = []
for i in reversed(range(len(lines[0]))):
    num = ""
    for j in range(len(lines)-1):
        if lines[j][i] != ' ':
            num += lines[j][i]
    if num != "":
        vert_nums.append(int(num))

    if(i < len(lines[-1]) and lines[-1][i] != ' '):
        if lines[-1][i] == '+':
            pt2 += sum(vert_nums)
        else:
            pt2 += math.prod(vert_nums)
        vert_nums.clear()

print("Part 2:", pt2)


