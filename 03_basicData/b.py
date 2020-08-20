from collections import deque

n,q = map(int,input().split())
a = deque(list(input().split()) for _ in range(n))
total = 0

while a:
    b = a.popleft()
    b[1] = int(b[1])
    if b[1] > q:
        b[1] -= q
        a.append(b)
        total += q
    else:
        total += b[1]
        b[1] = total
        print(*b)
        


