s, t= map(int, input().split())
# 変数sからまでの数でできる3組の非負整数の組み合わせの数を求める
n = 0
for i in range(s+1):
    for j in range(s+1):
        for k in range(s+1):
            if i+j+k <= s and i*j*k <= t:
                n += 1
print(n)