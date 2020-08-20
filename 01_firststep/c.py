n = int(input())
cnt = 0

for i in range(n):
    x = int(input())
    rt_x = int(pow(x,1/2)) +1
    flag = 1
    for j in range(2,rt_x):
        if x%j==0:
            flag = 0
            break
    cnt += flag
print(cnt)