k = (int(input()))
a, b = map(str, input().split())

# k進数でのaとbを10進数に変換
a10 = sum(int(a[-i-1]) * (k**i) for i in range(len(a)))
b10 = sum(int(b[-i-1]) * (k**i) for i in range(len(b)))

print(a10*b10)