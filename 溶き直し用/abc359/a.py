a, b = map(int, input().split())
ans = 0

for x in range(-100, 200):
    if (a - b) == (x - a) or (a - x) == (b - a) or \
       (b - a) == (x - b) or (b - x) == (a - b) or \
       (x - a) == (b - x) or (x - b) == (a - x):
        ans += 1

print(ans)