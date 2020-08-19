"""Binary Trees."""

class Node:
    def __init__(self, num, leftchild, rightchild):
        self.id = num
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = 'leaf'
        self.leftchild = leftchild
        self.rightchild = rightchild
        
    def show_info(self):
        print('node {}:'.format(self.id), 'parent = {},'.format(self.parent),
              'sibling = {},'.format(self.sibling),
              'degree = {},'.format(self.degree),
              'depth = {},'.format(self.depth),
              'height = {},'.format(self.height),
              '{}'.format(self.type))


def set_attributes(n_i, parent, sibling, depth):
    if n_i == -1:
        return -1
    node = T[n_i]
    lc = node.leftchild
    rc = node.rightchild
    node.parent = parent
    node.sibling = sibling
    node.depth = depth
    node.degree = (node.leftchild != -1) + (node.rightchild != -1)
    if lc != -1 or rc != -1:
        node.type = 'internal node'
    node.height = max(set_attributes(lc, n_i, rc, depth + 1),
                      set_attributes(rc, n_i, lc, depth + 1)) + 1
    return node.height



import sys

n = int(sys.stdin.readline())

T = [None] * n

rt_n = int(n * (n - 1) / 2)

for x in sys.stdin.readlines():
    num, leftchild, rightchild = list(map(int, x.split()))
    node = Node(num, leftchild, rightchild)
    T[num] = node
    rt_n -= (max(0, leftchild) + max(0, rightchild))

set_attributes(rt_n, -1, -1, 0)

T[rt_n].type = 'root'

for n in T:
    n.show_info()
