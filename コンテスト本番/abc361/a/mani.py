n,k,x= map(int, input().split())
# n個のスペース区切りの整数を入力
a= list(map(int, input().split()))
# aのk番目の直後にxを挿入
a.insert(k, x)
# aをスペース区切りで出力
print(*a)