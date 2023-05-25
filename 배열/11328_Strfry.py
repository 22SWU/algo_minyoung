N = int(input())
for i in range(0,N):
    a, b = input().split()
    newa=sorted(a)
    newb=sorted(b)
    if newa==newb:
        print("Possible")
    else:
        print("Impossible")