# 포인터 두개를 사용해야 하는 정렬
# 안그러면 시간초과됨...ㅠㅠ
N = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
answer = 0
left = 0
right = N-1
while left<right:
    plus = arr[left]+arr[right]
    if x==plus:
        answer +=1
    if plus<x:
        left +=1
    else:
        right -=1
print(answer)