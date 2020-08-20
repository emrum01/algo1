import math

def koch(n,p1,p2):

    sx = 2/3 * p1[0] + 1/3 * p2[0]
    sy = 2/3 * p1[1] + 1/3 * p2[1]
    s = (sx,sy)

    tx = 1/3 * p1[0] + 2/3 * p2[0]
    ty = 1/3 * p1[1] + 2/3 * p2[1]
    t = (tx,ty)

    theta = math.radians(60)
    ux = (tx - sx)*math.cos(theta) - (ty - sy)*math.sin(theta) + sx
    uy = (tx - sx)*math.sin(theta) + (ty - sy)*math.cos(theta) + sy
    u = (ux,uy)

    if n>0:
        koch(n-1,p1,s)
        print(*s)
        koch(n-1,s,u)
        print(*u)
        koch(n-1,u,t)
        print(*t)
        koch(n-1,t,p2)
    else: return

n = int(input())
a = [0.00000000,0.00000000]
b = [100.00000000,0.00000000]
print(*map(float,a))
koch(n,a,b)
print(*map(float,b))