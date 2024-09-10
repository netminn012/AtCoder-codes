l, r = map(int, input().split())
if l == r:
    print("Invalid")
else:
    if l == 1 and r == 0:
        print("Yes")
    else:
        print("No")
