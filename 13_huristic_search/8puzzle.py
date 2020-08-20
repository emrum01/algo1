from collections import deque
from functools import reduce

class State:
    def dup(self):
        ns = State()
        ns.b = []
        for row in self.b:
            ns.b.append(row[:])
        ns.z = self.z
        ns.c = self.c
        return ns

def read_board():
    s = State()
    s.b = [None] * 3
    for r in range(3):
        s.b[r] = [int(x) for x in input().split()]
        if 0 in s.b[r]:
            s.z = (r, s.b[r].index(0))
    s.c = 0
    return s

def move_zero(s, h):
    ns = s.dup()
    z = ns.z
    nz = (z[0] + h[0], z[1] + h[1])
    ns.b[nz[0]][nz[1]], ns.b[z[0]][z[1]] = ns.b[z[0]][z[1]], ns.b[nz[0]][nz[1]]
    ns.z = nz
    ns.c += 1
    return ns

def push_hands(q, s):
    if s.z[0] != 0:
        q.append(move_zero(s, (-1, 0)))
    if s.z[0] != 3 - 1:
        q.append(move_zero(s, (1, 0)))
    if s.z[1] != 0:
        q.append(move_zero(s, (0, -1)))
    if s.z[1] != 3 - 1:
        q.append(move_zero(s, (0, 1)))

def hash(b):
    return reduce(lambda acc, a: acc * 9 + a, sum(b, [])[:-1])

def solve(s):
    end = hash([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    hist = bytearray(hash([[8, 7, 6], [5, 4, 3], [2, 1, 0]]) + 1)
    q = deque([])
    while True:
        h = hash(s.b)
        if h == end:
            return s.c
        if not hist[h]:
            push_hands(q, s)
            hist[h] = True
        s = q.popleft()

def main():
    s = read_board()
    print(solve(s))

main()