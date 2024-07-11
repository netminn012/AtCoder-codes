a, b, c = map(int, input().split())
# a以上b以下であるようなcの倍数があるか
for i in range(a, b+1):
    if i % c == 0:
        print(i)
        exit()

print(-1)