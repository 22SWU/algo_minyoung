a = input()
b = input()
arr=[0]*26
answer = 0
for i in a:
    arr[ord(i)-97]+=1
for j in b:
    arr[ord(j)-97]-=1
for i in range(0,26):
    if arr[i]!=0:
        answer += abs(arr[i])
print(answer)