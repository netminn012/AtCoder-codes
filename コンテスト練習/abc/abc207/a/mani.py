a, b, c = map(int, input().split())
n = sorted([a, b, c])
max = n[-1] + n[-2]
print(max)