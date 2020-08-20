
def maxHeapify(i):
    l = 2*i
    r = 2*i+1

    if l<= H and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if  r <= H and a[r]> a[largest]:
        largest = r

    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        maxHeapify(largest)

def buildMaxHeap(a):
    i = H//2 
    while i>=1:
        maxHeapify(i)
        i -= 1
    
    

H = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
buildMaxHeap(a)
del a[0]
print(' ',end = "")
print(*a)

