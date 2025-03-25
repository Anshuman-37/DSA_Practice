import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    # We'll work with L = 61 bits (0-indexed positions 0..60)
    L = 61

    for _ in range(t):
        x = int(data[index]); y = int(data[index+1])
        index += 2
        # Quick check: if x == y then (x+k)==(y+k) so (x+k)&(y+k) = (x+k).
        # Since x >= 1, no k >=0 can make (x+k)==0. So impossible.
        if x == y:
            results.append("-1")
            continue

        # Precompute bits for x and y for positions 0 .. L-1
        bits_x = [(x >> i) & 1 for i in range(L)]
        bits_y = [(y >> i) & 1 for i in range(L)]

        # We want to compute k (in [0, 2^L)) so that for each bit i (from 0 to L-1),
        # if we add x and k (in binary, with carry) and similarly y and k,
        # then in the i-th bit of both sums, we never get both 1.
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(i, carry_x, carry_y):
            # i: current bit (0-indexed from LSB)
            # carry_x, carry_y: the carry coming from previous bits for x and y respectively.
            if i == L:
                # At the end, no extra carry must remain.
                if carry_x == 0 and carry_y == 0:
                    return 0
                else:
                    return None
            for b in (0, 1):
                # b will be the bit for k at position i.
                # Compute the sum for x:
                s_x = bits_x[i] + b + carry_x
                A = s_x & 1
                new_cx = s_x >> 1
                # Compute the sum for y:
                s_y = bits_y[i] + b + carry_y
                B = s_y & 1
                new_cy = s_y >> 1
                # We require that not (A == 1 and B == 1)
                if A == 1 and B == 1:
                    continue
                res = dp(i+1, new_cx, new_cy)
                if res is not None:
                    # Set the i-th bit of k to b and add the rest.
                    return (b << i) | res
            return None

        sol = dp(0, 0, 0)
        if sol is None or sol > 10**18:
            results.append("-1")
        else:
            results.append(str(sol))
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()