import sys

mys=list(sys.stdin.readline().strip())
mys2 = []
n = int(input())
cursor = len(mys)
for i in range(0, n):
    move = sys.stdin.readline().split()
    if move[0]=='L':
        if mys:
            mys2.append(mys.pop())

    elif move[0]=='D':
        if mys2:
            mys.append(mys2.pop())
    elif move[0]=='B':
        if mys:
            mys.pop()
    else:
        mys.append(move[1])
mys.extend(reversed(mys2))
print(''.join(mys))