import sys

n = int(input())

for i in range(0,n):
    password = input()
    answer = ""
    left = []
    right = []
    for j in password:
        if j == '-':
            if left:
                left.pop()
        elif j == '<':
            if left:
                right.append(left.pop())
        elif j == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(j)
    left.extend(reversed(right))
    print(''.join(left))

