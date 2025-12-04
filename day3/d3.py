
def findJoltage(bank: str) -> int:
    max = 0
    n = len(bank)
    for i in range(n):
        for j in range(i+1, n):
            if int(bank[i]+bank[j]) > max:
                max = int(bank[i]+bank[j])
    return max

def rec_solve(bank, k, cur):
    if k == 0:
        return int(cur)
    if k > len(bank):
        return -1
    include = rec_solve(bank[1:], k-1, cur+bank[0])
    exclude = rec_solve(bank[1:], k, cur)
    return max(include, exclude)

def dp_solve(bank, k):
    n = len(bank)

    #build a memoization table (k+1)*(n+1) dimensions
    memo = [[-1]*(k+1) for _ in range(n+1)]

    # picking 0 chars gives 0
    for i in range(n+1):
        memo[i][0] = 0

    for i in range(n-1, -1, -1):
        for j in range(1, k+1):
            if j > n - i:
                continue
            include_rest = memo[i+1][j-1]
            if include_rest != -1:
                include = int(bank[i]) * (10**(j-1))+include_rest
            else:
                include = -1

            exclude = memo[i+1][j]

            memo[i][j] = max(include, exclude)
    
    return memo[0][k]

dp_solve("234234234234278", 12)

with open("input", "r") as f:
    pt1 = 0
    pt2 = 0

    banks = f.read().strip().split("\n")
    for bank in banks:
        pt1 += findJoltage(bank)
    print("Part 1:", pt1)
    for bank in banks:
        pt2 += dp_solve(bank, 12)
    print("Part 2:", pt2)



