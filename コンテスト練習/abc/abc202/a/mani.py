# 入力
a, b, c = map(int, input().split())
# 変数a, b, cをそれぞれ7から引いた値にする
a, b, c = map(lambda x: 7-x, [a, b, c])
# 変数a, b, cを全部足した値を出力
print(a + b + c)