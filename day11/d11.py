from collections import deque
from typing import DefaultDict


with open("input", "r") as f:
    lines = f.read().strip().splitlines()

def count_paths(adj_list, start, end):
    q = deque([start])

    paths = 0
    while q:
        cur = q.popleft()
        if cur == end:
            paths += 1
        for n in adj_list[cur]:
                q.append(n)
    return paths


#DFS with memoization
def count_paths_2(adj_list, start, end, dac, fft):
    memo = {}
    def dfs(cur, dac_visited = False, fft_visited = False):
        key = (cur, dac_visited, fft_visited)
        if key in memo:
            return memo[key]
        
        if cur == end:
            return int(dac_visited and fft_visited)
        
        total = 0
        for n in adj_list[cur]:
            dac_visited_new = dac_visited or n==dac
            fft_visited_new = fft_visited or n==fft
            total += dfs(n, dac_visited_new, fft_visited_new)
        memo[key] = total
        return total
    return dfs(start)
        
        
nodes = {}
for i, line in enumerate(lines):
    node_name = line.split(" ")[0][:-1]
    nodes[node_name] = i

nodes['out'] = len(nodes)

adj_list = DefaultDict(list)
for i, line in enumerate(lines):
    neighbors = line.split(" ")[1:]
    for n in neighbors:
        idx = nodes[n]
        adj_list[i].append(idx)

# PART 1
start, end = nodes['you'], nodes['out']
pt1 = count_paths(adj_list, start, end)

#PART 2
start = nodes['svr']
end = nodes['out']
dac = nodes['dac']
fft = nodes['fft']
pt2 = count_paths_2(adj_list, start, end, dac, fft)

print(f"Part 1: {pt1}")
print(f"Part 2: {pt2}")

