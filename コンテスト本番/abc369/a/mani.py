a, b = map(int, input().split())
x = 0

# a b xで作れる等差数列のxがなんとうりかを求める。 a b xはすべて整数である。

if (b - a) % x == 0:
  print((b - a) // x +1 )
else:
  print((b - a) // x + 2)