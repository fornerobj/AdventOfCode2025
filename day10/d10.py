from collections import deque
import re, z3

with open("input", "r") as f:
    machines = f.read().strip().splitlines()

def press_button(current, button):
    new = list(current)
    for b in button:
        new[b] *= -1
    return tuple(new)

def count_button_presses(goal, buttons):
    n = len(goal)
    lights = tuple([-1 for _ in range(n)])
    
    q = deque([(lights, 0)])
    seen = {lights}

    while q:
        cur, presses = q.popleft()

        if cur == goal:
            return presses

        for button in buttons:
            new_lights = press_button(cur, button)
            if new_lights not in seen:
                seen.add(new_lights)
                q.append((new_lights, presses+1))
    return -1

def solve_system(goal, buttons):
    o = z3.Optimize()
    vars = z3.Ints(f"n{i}" for i in range(len(buttons)))
    for var in vars: o.add(var >= 0)
    for i, joltage in enumerate(goal):
        equation = 0
        for b, button in enumerate(buttons):
            if i in button:
                equation += vars[b]
        o.add(equation == joltage)
    o.minimize(sum(vars))
    o.check()
    return o.model().eval(sum(vars)).as_long()


pt1 = 0
pt2 = 0
for machine in machines:
    components = machine.split(" ")
    goal = tuple([1 if x == '#' else -1 for x in components[0][1:-1]])
    joltage_goal = [int(x) for x in components[-1][1:-1].split(",")]
    n = len(goal)
    buttons = [list(int(x) for x in button.strip("()").split(",")) for button in components[1:-1]]
    pt1 += count_button_presses(goal, buttons)
    pt2 += solve_system(joltage_goal, buttons)

print(f"Part 1: {pt1}")
print(f"Part 2: {pt2}")




