SAB,SAC,SBC=map(input().split())
# 三人の兄弟ABCで以下の年齢関係がある
# SABが<ならば、AのBより年下、>ならば年上
# SACが<ならば、AのCより年下、>ならば年上
# SBCが<ならば、BのCより年下、>ならば年上
# なお矛盾することはない

# 三人のなかで二番目に年上の人を求める

# 三人の年齢関係を比較する
if SAB==">" and SAC==">" and SBC==">":
    print("A")
    print("B")
    print("C")
elif SAB==">" and SAC=="<" and SBC==">":
    print("A")
    print("C")
    print("B")
elif SAB==">" and SAC==">" and SBC=="<":
    print("B")
    print("A")
    print("C")

elif SAB=="<" and SAC==">" and SBC==">":
    print("C")
    print("A")
    print("B")