with open("input", "r") as file:
    cur = 50
    ans = 0
    for line in file:
        line = line.strip()
        dir = line[0]
        amount = int(line[1:])

        # A full rotation will always cross 0
        if(amount > 100):
            ans += amount // 100

        if(dir == 'R'):
            if (cur + (amount%100) >= 100):
                if(cur != 0):
                    ans += 1
            cur = (cur + amount) % 100
        else:
            if (cur - (amount%100) <= 0):
                if(cur != 0):
                    ans += 1
            cur = (cur - amount) % 100

print(ans)

