A = int(input())
B = int(input())
C = int(input())
answer = [0]*10
total = str(A*B*C)
for i in total:
    answer[int(i)]+=1
for i in range(10):
    print(answer[i])