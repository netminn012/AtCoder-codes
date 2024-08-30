n,k = map(int, input().split())
a=list(map(int, input().split()))

# aから下からk枚分を取り出し、一番上に移動させたリストAを作る
A = a[n-k:]
print(*A)