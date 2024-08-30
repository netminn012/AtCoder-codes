n = input()
# pは空白区切りの整数
p= list(map(int, input().split()))
# pをリストにする
q = [0]*len(p)

# 全てのiに対して Pi=i がなりたつものを探して、成り立たないものを消す
for i in range(len(p)):
    q[p[i]-1] = i+1

print(*q)