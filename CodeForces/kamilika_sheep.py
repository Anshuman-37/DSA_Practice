import sys

def solve():
    """
    Solves a single test case.
    """
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    min_beauty = min(a)
    max_beauty = max(a)

    max_pleasure = max_beauty - min_beauty

    print(max_pleasure)

t = int(sys.stdin.readline())

for _ in range(t):
    solve()