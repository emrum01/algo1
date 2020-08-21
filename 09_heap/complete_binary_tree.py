'''
n = int(input())
a = [0] + input().split()

for i in range(1,n+1):
    print(f'node {i}: key = {a[i]}, ',end ="")
    print(f'parent key = {a[i//2]}, 'if i>1 else "",end = "")
    print(f'left key = {a[2*i]}, 'if 2*i<=n else "",end = "")
    print(f'right key = {a[2*i + 1]}, ' if  2*i + 1<=n  else "")
'''
class node:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
class comp_binary_tree:
    def __init__(self,b):
        self.array = b
        
    def getinfo(self,a):
        for i in range(n//2-1):
            if i!=0:
                a[i].parent = a[i//2]
            if a[2*i + 1]:
                a[i].left = a[2*i]
                a[i].right = a[2*i + 1]
        
        
n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
    b.append(node(i))
c = comp_binary_tree(b)
c.getinfo(b)

for i in range(n):
    print(f'node {i}: key = {b[i].key}, ',end ="")
    print(f'parent key = {b[i].parent}, 'if b[i] is not None else "",end = "")
    print(f'left key = {b[i].left}, 'if b[i].left is not None else "",end = "")
    print(f'right key = {b[i].right}, ' if b[i].right is not None else "")

    


         