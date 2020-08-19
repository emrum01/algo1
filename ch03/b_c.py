class queue:
    def __init__(self,data=[]):
        self.data = data
    def push(self,x):
        self.data.append(x)
        return
    def pop(self):
        if len(self.data)==0:
            return "empty"
        return self.data.pop(0)
    def len(self):
        return len(self.data)

q = queue()
n,t = map(int, input().split())
for i in range(n):
    name,time = input().split()
    time = int(time)
    q.push([name,time])
i = 0
total = 0
while q.len()>0:
    p = q.pop()
    spend = min(t,p[1])
    p[1] -= spend
    total += spend
    if(p[1]==0):
        print(p[0],total)
    else:
        q.push(p)