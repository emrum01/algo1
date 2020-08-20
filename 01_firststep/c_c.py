n = int(input())
x = [int(input()) for _ in range(n)]
answer = 0
for i in range(n):
    isPrime = 1
    for j in range(2,int(pow(x[i],1/2))+1): #a[i]==2の時、range(2,2)となってループが実行されない
        if x[i]%j == 0:                     #pow関数でintにキャストしているのは少数を切り捨てるため
            isPrime = 0                     #平方根に1を足しているのは、ループを起動させて計算を成功させるため
            break
    answer += isPrime
print(answer)
