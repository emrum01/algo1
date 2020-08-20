import math

def merge(a, l, mid, r):
    global cnt
    L = a[l:mid] + [math.inf]
    R = a[mid:r] + [math.inf]
    i = 0
    j = 0
    for k in range(l,r):
        cnt += 1
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1 
    print(*a)

def mergeSort(a,l,r):
    if l+1 < r:
        mid =(l + r)//2
        mergeSort(a,l,mid)
        print('left: ',end = "")
        print(*a)
        mergeSort(a,mid,r)
        print('right: ',end = "")
        print(*a)
        merge(a,l,mid,r)

n = int(input())
a = list(map(int, input().split()))
cnt = 0
mergeSort(a,0,n)
print(' '.join([str(i) for i in a]))
print(cnt)
