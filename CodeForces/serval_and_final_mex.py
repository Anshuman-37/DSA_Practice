def mex(arr):
    s = set(arr)
    m = 0
    while m in s:
        m += 1
    return m

def is_target(arr):
    # For an array of length L, the target is [1,2,...,L]
    L = len(arr)
    return arr == list(range(1, L+1))

import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    pos = 1
    out_lines = []
    for _ in range(t):
        n = int(data[pos]); pos += 1
        # read array a (as list of ints)
        a = list(map(int, data[pos:pos+n])); pos += n
        ops = []  # list of (l, r) operations (1-indexed)
        # We use a list "a" and update it by simulating a “replacement‐and–deletion” operation.
        # (This simulation is equivalent to the standard greedy solution.)
        while not is_target(a) and len(a) >= 2:
            L = len(a)
            m = mex(a)
            if m < L:
                # We want to “fix” position m so that a[m] becomes m+1.
                # (In the target we want a[i] = i+1.)
                if m < L - 1:
                    # simulate a replacement on a[m] by choosing segment [m, m+1]
                    l_idx, r_idx = m, m+1
                    # output operation using 1-indexing: (m+1, m+2)
                    ops.append((l_idx+1, r_idx+1))
                else:
                    # m == L-1; choose segment (m-1, m) in 0-index (i.e. (m, m+1) in 1-indexed)
                    l_idx, r_idx = m-1, m
                    ops.append((l_idx+1, r_idx+1))
                    # In this branch we will “fix” position m-1.
                    m = m - 1
                # In the standard solution, we set a[m] = m+1.
                # To simulate a replacement operation (which must reduce the array’s length by 1),
                # we remove the element at position m+1 and update a[m].
                new_val = m + 1
                # Update: a becomes a[0:m] + [new_val] + a[m+2:]
                a = a[:m] + [new_val] + a[m+2:]
            else:
                # m == L.
                # There is at least one index i with a[i] != i+1.
                # Let i be the first such index.
                i = 0
                while i < L and a[i] == i+1:
                    i += 1
                # Now, we choose the operation on the segment from i to the end.
                ops.append((i+1, L))
                # In the standard solution, we then set all a[i...L-1] = i+1.
                a = a[:i] + [i+1]
        # When the while–loop ends we have either len(a)==1 or a is target (i.e. a = [1,2,...,L] with L>=2).
        if len(a) >= 2:
            # Final operation on the entire array makes its mex equal to 0.
            ops.append((1, len(a)))
            a = [mex(a)]  # This will be [0] because a is [1,2,...,L] so mex = 0.
        # (If len(a)==1 already, then a must be [0].)
        # Output the operations.
        out_lines.append(str(len(ops)))
        for l, r in ops:
            # It must hold that l < r.
            # (Our simulation guarantees that because when simulating a single–element op we always use two consecutive indices.)
            out_lines.append(f"{l} {r}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()