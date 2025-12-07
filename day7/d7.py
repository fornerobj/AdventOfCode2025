from collections import defaultdict


def count_splits(grid):
    rows, cols = len(grid), len(grid[0])
    start = grid[0].find('S')

    visited = set()

    def traverse(y,x):
        if not (0 <= x < cols and 0 <= y < rows):
            return
        cell = grid[y][x]

        if cell == '^':
            if (y,x) in visited:
                return

            visited.add((y,x))

            traverse(y+1, x-1)
            traverse(y+1, x+1)
        else:
            traverse(y+1, x)

    traverse(1, start)
    return len(visited)

def count_paths(grid):
    rows, cols = len(grid), len(grid[0])
    start = grid[0].find('S')


    memo = {}
    def traverse(y,x) -> int:
        if((y,x) in memo):
            return memo[(y,x)]
        if not (0 <= x < cols and 0 <= y < rows):
            memo[(y,x)] = 1
            return 1

        cell = grid[y][x]

        if cell == '^':
            left = traverse(y+1, x-1)
            right = traverse(y+1, x+1)
            memo[(y,x)] = left+right

        else:
            memo[(y,x)] = traverse(y+1, x)

        return memo[(y,x)]

    return(traverse(1, start))
    

with open("input", "r") as f:
    grid = f.read().strip().splitlines()

pt1 = count_splits(grid)
print("Part 1:", pt1)
pt2 = count_paths(grid)
print("Part 2:", pt2)
