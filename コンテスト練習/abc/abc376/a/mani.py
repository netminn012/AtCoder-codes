n, c = map(int, input().split())
t = list(map(int, input().split()))
getkaisuuu = 1  # 最初のボタン押しで飴をもらう

for i in range(1, n):
    if t[i] - t[i - 1] >= c:
        getkaisuuu += 1

print(getkaisuuu)