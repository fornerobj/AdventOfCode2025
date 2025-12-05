def check_in_range(range, ingredient):
    l,h = range
    if int(ingredient) >= l and int(ingredient) <= h:
        return True
    return False

def reduce_ranges(fresh):
    fresh = sorted(fresh)
    i = 0
    while i < len(fresh)-1:
        l1, h1 = fresh[i]
        l2, h2 = fresh[i+1]
        if h1 < l2:
            i+=1
            continue
        elif h1 >= l2:
            fresh.pop(i)
            fresh.pop(i)
            if h1 <= h2:
                fresh.insert(i, (l1,h2))
            else:
                fresh.insert(i, (l1,h1))
    return fresh

with open("input", "r") as f:
    db = f.read().strip()
    ranges, ingredients = db.split("\n\n")

    fresh = []
    for r in ranges.splitlines():
        l, h = r.split("-")
        l, h = int(l), int(h)
        fresh.append((l,h))
    fresh = reduce_ranges(fresh)

    pt1 = 0
    for ing in ingredients.splitlines():
        for f in fresh:
            if check_in_range(f, ing):
                pt1 += 1
                break
    print("Part 1:", pt1)

    pt2 = 0
    for r in fresh:
        pt2 += r[1] - r[0] + 1

    print("Part 2:", pt2)

