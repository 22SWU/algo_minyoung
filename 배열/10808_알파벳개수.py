# 알파벳은 26개
str = input()
alpha = [0]*26
for i in str:
    alpha[ord(i)-97]+=1

print(*alpha)
