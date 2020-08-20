def gcd(x,y):
    if x<y:
        x,y = y,x
    if y==0:
       return x
    if x==y:
        return x
    return gcd(y,x%y)


    
x,y = map(int,input().split())
print(gcd(x,y))

