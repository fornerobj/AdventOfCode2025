from collections import deque
import math

with open("input", "r") as f:
    data = f.read().strip()

positions = [tuple(int(x) for x in line.split(",")) for line in data.splitlines()]
n = len(positions)

pos_id = {p: i for i, p in enumerate(positions)}

class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.num_components = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra==rb:
            return False
        
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.num_components -= 1
        return True

    def component_sizes(self):
        roots = {}
        for i in range(n):
            r = self.find(i)
            roots[r] = roots.get(r,0) + 1
        return sorted(roots.values(), reverse=True)

pairs = []
for i in range(n):
    for j in range(i+1, n):
        dist = math.dist(positions[i], positions[j])
        pairs.append((dist,i,j))
pairs.sort(key=lambda x: x[0])

dsu = DSU(n)

pt1 = None
pt2 = None

for i, (dist, a, b) in enumerate(pairs):
    merged = dsu.union(a,b)

    if i == 1000 and pt1 is None:
        sizes = dsu.component_sizes()
        pt1 = sizes[0]*sizes[1]*sizes[2]

    if dsu.num_components == 1:
        p1, p2 = positions[a], positions[b]
        pt2 = p1[0]*p2[0]

print("Part 1:", pt1)
print("Part 2:", pt2)
