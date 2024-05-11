#N X Y Z
# スペース区切りの整数の入力
n,x,y,z= map(int, input().split())

#上り下り判定
if x>y:
    if x<z and z<y:
        print("Yes")
    else:
        print("No")
else:
    if x>z>y:
        print("Yes")
    else:
        print("No")


''''''
if x <= z <= y:
    print("Yes")
else:
    print("No")
''''''
#print("{} {}".format(a+b+c))
