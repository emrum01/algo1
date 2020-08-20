from collections import namedtuple

Pos = namedtuple("Pos", "r c")
def read_queens():
    qs = []
    k = int(input())
    for _ in range(k):
        r, c = [int(x) for x in input().split()]
        qs.append(Pos(r, c))
    return qs

def print_board(qs):
    for r in range(8):
        for c in range(8):
            print("Q" if (Pos(r, c) in qs) else ".", end="")
        print()

def is_attacked(p, qs):
    return (
        (p.r in [q.r for q in qs])
        or (p.c in [q.c for q in qs])
        or (any([abs(p.r - q.r) == abs(p.c - q.c) for q in qs]))
    )
def eight_queens(qs):
    def rec(p, qs):
        if len(qs) == 8:
            return qs
        elif over(p):
            return False
        elif is_attacked(p, qs):
            return rec(next_sq(p), qs)
        else:
            result = rec(Pos(p.r + 1, 0), qs + [p])
            return result if result else rec(next_sq(p), qs)

    return rec(Pos(0, 0), qs)

def next_sq(p):
    if p.c == 7:
        return Pos(p.r + 1, 0)
    else:
        return Pos(p.r, p.c + 1)

def over(p):
    return p.r > 7
def main():
    qs = read_queens()
    print_board(eight_queens(qs))

main()