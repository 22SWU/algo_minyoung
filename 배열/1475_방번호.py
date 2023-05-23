room = input()
number = [0]*9
six = 0
for i in room:
    if int(i)==6 or int(i)==9:
        six+=1
    else:
        number[int(i)]+=1
if six%2!=0:
    six = six//2+1
else:
    six//=2
a = max(number)
print(max(a, six))