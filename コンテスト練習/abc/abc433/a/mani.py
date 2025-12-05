x,y,z = map(int, input().split())

# 100歳までの間でxがyのちょうどz倍になることがあるか
if any(x + i == (y + i) * z for i in range(101)):
    print("Yes")
else:
    print("No")

