n = int(input())
a = [list(map(int,input().split())) for i in range(n)]

matrix = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    if len(a[i])>2:
        b = a[i][2:]   
        for j in b:
            matrix[i][j-1] = 1
    print(*matrix[i])