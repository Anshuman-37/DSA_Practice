import sys

def solve():
    n = int(sys.stdin.readline())
    a_str = sys.stdin.readline().strip()
    b_str = sys.stdin.readline().strip()
    # Convert strings to lists of integers (0 or 1)
    a = [int(c) for c in a_str]
    b = [int(c) for c in b_str]

    # Calculate the number of 'a' positions in each component
    # Component E: a[0], a[2], ...
    nodes_a_E = (n + 1) // 2
    # Component O: a[1], a[3], ...
    nodes_a_O = n // 2

    # Calculate the total number of zeros in each component
    zeros_E = 0
    zeros_O = 0

    for k in range(n):
        # Check Component E: {a[k] | k even} U {b[k] | k odd}
        if k % 2 == 0: # k is even
            if a[k] == 0:
                zeros_E += 1
        else: # k is odd
            if b[k] == 0:
                zeros_E += 1

        # Check Component O: {a[k] | k odd} U {b[k] | k even}
        if k % 2 != 0: # k is odd
            if a[k] == 0:
                zeros_O += 1
        else: # k is even
            if b[k] == 0:
                zeros_O += 1

    possible_E = (zeros_E >= nodes_a_E)
    possible_O = (zeros_O >= nodes_a_O)

    if possible_E and possible_O:
        print("YES")
    else:
        print("NO")

t = int(sys.stdin.readline())
for _ in range(t):
    solve()