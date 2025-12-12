from collections import deque

with open("input", "r") as f:
    data = f.read().strip()

def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    length = abs(x2-x1)+1
    width = abs(y2-y1)+1
    return length*width

positions = [tuple(int(x) for x in line.split(",")) for line in data.splitlines()]
n = len(positions)

# Part 2 solution copied from HyperNeutrino on Youtube!
xs = sorted ({x for x, _ in positions})
ys = sorted ({y for _, y in positions})

grid = [[0] * (len(xs) * 2 -1) for _ in range(len(ys)*2-1)]

for (x1, y1), (x2,y2) in zip(positions, positions[1:] + positions[:1]):
    cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
    for cx in range(cx1, cx2+1):
        for cy in range(cy1, cy2+1):
            grid[cy][cx] = 1

outside = {(-1,-1)}
q = deque(outside)

while q:
    tx, ty = q.popleft()
    for nx, ny in [(tx-1, ty), (tx+1, ty), (tx, ty-1), (tx, ty+1)]:
        if nx < -1 or ny < -1 or nx > len(grid[0]) or ny > len(grid):
            continue
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == 1:
            continue
        if (nx, ny) in outside:
            continue
        outside.add((nx,ny))
        q.append((nx,ny))

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x,y) not in outside:
            grid[y][x] = 1

psa = [[0]*len(row) for row in grid]
for y in range(len(psa)):
    for x in range(len(psa[0])):
        left = psa[y][x-1] if x > 0 else 0
        top = psa[y-1][x] if y > 0 else 0
        topleft = psa[y-1][x-1] if (x > 0 and y > 0) else 0
        psa[y][x] = left + top - topleft + grid[y][x]

def validate(psa, x1, y1, x2, y2):
    cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
    left = psa[cy2][cx1-1] if cx1 > 0 else 0
    top = psa[cy1-1][cx2] if cy1 > 0 else 0
    topleft = psa[cy1-1][cx1-1] if (cx1 > 0 and cy2 > 0) else 0
    return (psa[cy2][cx2] - left - top + topleft) == area((cx1, cy1), (cx2,cy2))

pt1 = -1
pt2 = -1
for i in range(n):
    for j in range(i+1, n):
        p1 = positions[i]
        p2 = positions[j]
        pt1 = max(pt1, area(p1,p2))
        if validate(psa, p1[0], p1[1], p2[0], p2[1]):
            pt2 = max(pt2, area(p1,p2))

print(f"Part 1: {pt1}")
print(f"Part 2: {pt2}")

