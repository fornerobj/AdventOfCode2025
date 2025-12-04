dirs = [(-1, 1), (0, 1), (1,1), (1,0), (1,-1), (0, -1), (-1,-1), (-1, 0)]

def check(grid, x, y):
    if grid[y][x] != '@':
        return False
    adj = 0
    for dir in dirs:
        dx, dy = dir
        newx, newy = x+dx, y+dy
        if newx < 0 or newx >= len(grid[0]):
            continue
        if newy < 0 or newy >= len(grid):
            continue
        if grid[newy][newx] == '@':
            adj += 1
    return adj < 4

def get_pos_to_remove(grid):
    to_remove = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '@':
                continue
            if check(grid, x, y):
                to_remove.add((y,x))
    return to_remove

with open("input", "r") as f:
    grid = f.read().strip().splitlines()
    pt1 = len(get_pos_to_remove(grid))
    pt2 = 0
    while True:
        to_remove = get_pos_to_remove(grid)
        if len(to_remove) <= 0:
            break
        pt2 += len(to_remove)
        for (y,x) in to_remove:
            grid[y] = grid[y][:x] + '.' + grid[y][x+1:]

print("Part 1:", pt1)
print("Part 2:", pt2)


    
