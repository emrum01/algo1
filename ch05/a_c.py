n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

s={0}
for i in a:
    s |= {i+ x for x in s} #論理和にすることで、集合単位で演算できる

for i in m:
    if i in s:
        print('yes')
    else:
        print('no') 