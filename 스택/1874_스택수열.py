N = int(input())
stack = []
answer = []
cursor = 1
pos = 0
for i in range(N):
    num = int(input())
    while cursor<=num:
        stack.append(cursor)
        answer.append("+")
        cursor += 1
    if stack[-1]==num:
        stack.pop()
        answer.append("-")
    else:
        pos = 1
if pos == 0:
    for i in answer:
        print(i)
else:
    print("NO")