def gcd(x,y):
    if y>x:
        x,y = y,x
    if y==0:
        return x
    elif x==y:
        return x
    else:
        return gcd(y,x%y)

x,y = map(int,input().split())
print(gcd(x,y))
