N = int(input())
answer = []
for i in range(0, N):
    num = int(input())
    if num == 0:
        answer.pop(-1)
    else:
        answer.append(num)
print(sum(answer))