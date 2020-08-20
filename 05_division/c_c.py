import math 

def koch(a,b,num):

    sx = 2 / 3 * a[0] + 1 / 3 * b[0]
    sy = 2 / 3 * a[1] + 1 / 3 * b[1]
    s = (sx, sy)

    tx = 1 / 3 * a[0] + 2 / 3 * b[0]
    ty = 1 / 3 * a[1] + 2 / 3 * b[1]
    t = (tx, ty)

    theta = math.radians(60)
    ux = math.cos(theta) * (tx - sx) - math.sin(theta) * (ty - sy) + sx
    uy = math.sin(theta) * (tx - sx) + math.cos(theta) * (ty - sy) + sy
    u = (ux, uy)
    if num > 0:
        koch(a,s,num-1)
        print(*s)
        koch(s,u,num-1)
        print(*u)
        koch(u,t,num-1)
        print(*t)
        koch(t,b,num-1)
    else:
        return

n = int(input())
a = [0.00000000,0.00000000]
b = [100.00000000,0.00000000]
print(*map(float,a))
koch(a,b,n)
print(*map(float,b))