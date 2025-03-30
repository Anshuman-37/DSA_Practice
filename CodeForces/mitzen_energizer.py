import sys
from collections import Counter

def solve():
    n = int(sys.stdin.readline())
    s_str = sys.stdin.readline().strip()
    s = list(s_str) # Work with a list for insertions

    # --- Edge Case: n=1 ---
    # Cannot perform any operation if length is 1.
    # It's only balanced if n=0, which is not allowed by constraints.
    if n == 1:
        print("-1")
        return

    # Calculate initial counts
    counts = Counter(s_str)
    count_l = counts.get('L', 0)
    count_i = counts.get('I', 0)
    count_t = counts.get('T', 0)

    # --- Edge Case: Monolithic String ---
    # If all characters are the same, no s[i] != s[i+1] exists.
    # If it's not already balanced (which it can't be if n>0 and monolithic),
    # it's impossible.
    if len(counts) == 1 and n > 0:
        print("-1")
        return

    # --- Calculate Target State ---
    # Find the max count among L, I, T
    max_initial_count = 0
    if n > 0:
        max_initial_count = max(count_l, count_i, count_t)

    # Target length N must be >= n and >= 3 * max_initial_count
    n_candidate = max(n, 3 * max_initial_count)

    # Target length N must be a multiple of 3
    target_n = n_candidate
    if target_n % 3 != 0:
        target_n += (3 - (target_n % 3))

    # Target count k for each character
    target_k = target_n // 3

    # --- Check if already balanced ---
    if count_l == target_k and count_i == target_k and count_t == target_k:
        print("0")
        return

    # Calculate how many of each character we need to add
    needed = {
        'L': target_k - count_l,
        'I': target_k - count_i,
        'T': target_k - count_t
    }

    # Basic sanity check (shouldn't fail with correct target calculation)
    if needed['L'] < 0 or needed['I'] < 0 or needed['T'] < 0:
        print("-1") # Should not happen
        return

    operations_log = []
    all_chars = {'L', 'I', 'T'}

    # --- Perform Operations (Greedy Strategy: Insert Needed Character) ---
    # Loop until all needed characters have been inserted
    while needed['L'] > 0 or needed['I'] > 0 or needed['T'] > 0:
        inserted_this_pass = False
        # Iterate through possible insertion points (indices 0 to len(s)-2)
        # Use length at the start of the pass for the loop range
        current_len = len(s)
        for j in range(current_len - 1):
            # Check if insertion is possible at index j+1 (between s[j] and s[j+1])
            if s[j] != s[j+1]:
                # Determine character x that *would* be inserted
                pair_chars = {s[j], s[j+1]}
                # Find the single character in all_chars but not in pair_chars
                x = list(all_chars - pair_chars)[0]

                # Check if this character x is one we currently need
                if needed[x] > 0:
                    # Perform the insertion
                    s.insert(j + 1, x)
                    operations_log.append(j + 1) # Record 1-based index
                    needed[x] -= 1 # Decrement the count for the needed char
                    inserted_this_pass = True
                    # IMPORTANT: Break inner loop and restart scan from beginning
                    # because indices have shifted and new pairs are formed.
                    break

        # If a full pass through the current string occurred
        # without finding any place to insert a *needed* character:
        if not inserted_this_pass:
            # We are stuck according to the greedy strategy. Assume impossible.
            print("-1")
            return

    print(len(operations_log))
    for op_index in operations_log:
        print(op_index)


t = int(sys.stdin.readline())
for _ in range(t):
    solve()