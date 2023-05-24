num, k = map(int, input().split())
answer = 0
girl = [0]*6
boy = [0]*6
for i in range(0,num):
    gen, gra = map(int, input().split())
    if gen == 0:
        girl[gra-1]+=1
    else:
        boy[gra-1]+=1
for i in range(0,6):
    if girl[i]!=0:
        if girl[i]%k!=0:
            answer += girl[i]//k+1
        else:
            answer += girl[i]//k
    if boy[i]!=0:
        if boy[i]%k!=0:
            answer += boy[i]//k+1
        else:
            answer += boy[i]//k
print(answer)