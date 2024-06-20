a, b= map(int, input().split())
if a<=b:
    count = b - a + 1
    print(count)
else:
    print(0)