n = int(input())
a = list(map(int,input().split()))
q = int(input())
b = list(map(int,input().split()))

sumn = {0}
for i in a:
    sumn |= {i + x for x in sumn}
print(sumn)
for i in b:
    if i in sumn:
        print('yes')
    else:
        print('no')
