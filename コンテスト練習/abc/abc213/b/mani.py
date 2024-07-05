n = int(input())
a = list(map(int, input().split())) 
# aのインデックスの入ったリストを作成
index = [i for i in range(n)]
# aとindexをソート
a, index = zip(*sorted(zip(a, index), reverse=True))
# indexの2番目を出力
print(index[1]+1)