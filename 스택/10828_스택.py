import sys

N = int(input())
arr = []
answer = []

for i in range(0,N):
    com = sys.stdin.readline().split()
    if com[0]=='push':
        arr.append(com[1])

    elif com[0] == 'pop':
        if len(arr)>0:
            answer.append(arr.pop(-1))
        else:
            answer.append(-1)
    
    elif com[0] == 'size':
        answer.append(len(arr))

    elif com[0] == 'empty':
        if len(arr)>0:
            answer.append(0)
        else:
            answer.append(1)
    else:
        if len(arr)>=1:
            answer.append(arr[-1])
        else:
            answer.append(-1)
for i in answer:
    print(i)