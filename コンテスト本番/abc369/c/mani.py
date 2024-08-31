n = int(input())
a= []

# 1≤l≤r≤Nを満たす組 (l,r) について、数列(ai,ai+1,…,aj) が等差数列であるようなものは何通りあるか求めてください。
'''
入力例 1
4
3 6 9 3

出力例 1
8
'''

a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] * 2 == a[j]:
            ans += 1
            break
print(ans)