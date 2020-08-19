
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j][1] <= x[1]:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1
    
def quickSort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
        
n = int(input())
data = []
for i in range(n):
    m,num = map(str,input().split())
    data.append([m, int(num)])
data1 = data[:]

quickSort(data,0,n-1)

for i in range(n-1):
    if data[i][1] == data[i+1][1]:
        if data1.index(data[i]) > data1.index(data[i+1]):
            print("Not stable")
            break
else:
    print("Stable")

for i in data:
    print(' '.join(str(d) for d in i))
