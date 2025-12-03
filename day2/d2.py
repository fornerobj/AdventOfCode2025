def checkValid(id):
    n = len(id)
    for i in range(1, n//2+1):
        if n % i != 0:
            continue
        chunks = [id[j:j+i] for j in range(0, len(id), i)]
        match = chunks[0]
        matching = True
        for k in range(1, len(chunks)):
            if chunks[k] != match:
                matching = False
                break
        if matching:
            return True
    return False
                

with open("input", "r") as f:
    data = f.read().strip()
    ranges = data.split(",")
    ans = 0
    for r in ranges:
        low, high = r.split("-")
        low = int(low)
        high = int(high) + 1
        for i in range(low, high):
            if checkValid(str(i)):
                ans += i

print(ans)
