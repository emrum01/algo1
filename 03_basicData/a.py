a = input()
b = []
for i in a:
    if i in '+-*':
        n1 = b.pop()
        n2 = b.pop()
        b.append(eval(n2+i+n1))
    b.append(i)
print(b.pop())