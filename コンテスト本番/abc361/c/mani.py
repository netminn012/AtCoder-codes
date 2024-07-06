n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()  # a をソート

min_diff = float('inf')
for i in range(k + 1):
    diff = a[i + n - k - 1] - a[i]  # 連続する n-k 個の要素の最大値と最小値の差
    min_diff = min(min_diff, diff)  # 最小の差を更新

print(min_diff)