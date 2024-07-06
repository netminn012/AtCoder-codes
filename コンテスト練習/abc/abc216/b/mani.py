n = input(int())
s = [input().split() for i in range(n)]
for i in range(n):
    if s[i][0] == "Y":
        print(s[i][1])
        exit()
print("No")