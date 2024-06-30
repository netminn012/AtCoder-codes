n = int(input())
numbers = list(map(int, input().split()))

# 各色のインデックスを格納する辞書を作成
color_indices = {}
for index, color in enumerate(numbers):
    if color not in color_indices:
        color_indices[color] = []
    color_indices[color].append(index)

# 条件を満たす組み合わせの数をカウント
count = 0
for indices in color_indices.values():
    for i in range(len(indices) - 1):
        if indices[i + 1] - indices[i] == 2:
            count += 1

print(count)