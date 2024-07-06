a,b,c,d,e,f= map(int, input().split())
g,h,i,j,k,l= map(int, input().split())
# 2つの直方体c(a,b,c,d,e,f)とc(g,h,i,j,k,l)の共通部分の体積が正かどうか yes or no

# x,y,z軸それぞれで共通部分が存在するか判定
if (min(d,j) > max(a,g)) and (min(e,k) > max(b,h)) and (min(f,l) > max(c,i)):
  print("Yes")
else:
  print("No")