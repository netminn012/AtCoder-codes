s, t = input().split()

for w in range(1, len(s)): # w は 1 文字区切りから len(s)-1区切りまで
    for c in range(1 , w+1):
        result = ''
        for i in range(c - 1, len(s), w):
            if i + w <= len(s):
                result += s[i]
        
        if result == t:
            print("Yes")
            exit()

print("No")