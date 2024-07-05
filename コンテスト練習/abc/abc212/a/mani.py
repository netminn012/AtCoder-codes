a, b= map(int, input().split())
# 出力
if 0 < a and b == 0:
    print('Gold')
elif a == 0 and 0 < b:
    print('Silver')
else:
    print('Alloy')