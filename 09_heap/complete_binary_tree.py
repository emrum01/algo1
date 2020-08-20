n = int(input())
a = [0] + input().split()

for i in range(1,n+1):
    print(f'node {i}: key = {a[i]}, ',end ="")
    print(f'parent key = {a[i//2]}, 'if i>1 else "",end = "")
    print(f'left key = {a[2*i]}, 'if 2*i<=n else "",end = "")
    print(f'right key = {a[2*i + 1]}, ' if  2*i + 1<=n  else "")
