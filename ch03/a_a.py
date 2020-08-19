
class stack:
    def __init__(self, data = []):
        self.data = data
    def push(self,x):
        self.data.append(x)
    
    def pop(self):
        if len(self.data)==0:
            return "empty!"
        else:
            cell = self.data.pop()
            return cell
i = 0
a = list(input().split())
s = stack()
for i in a:
    if i in '+-*':
        c = s.pop()
        d = s.pop()
        s.push(str(eval(d+i+c)))
    else:
        s.push(i)
print(s.pop())

