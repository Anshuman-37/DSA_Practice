def is_universal(s):
    # A string is universal if it is lexicographically smaller than its reversal.
    return s < s[::-1]

import sys
input_data = sys.stdin.read().split()
if not input_data:
    exit(0)

t = int(input_data[0])
index = 1
results = []

for _ in range(t):
    n = int(input_data[index])
    k = int(input_data[index+1])
    s = input_data[index+2]
    index += 3

    # Case 1: Already universal.
    if is_universal(s):
        results.append("YES")
        continue

    # Case 2: If all characters are the same, no swap can change the fact that s equals its reversal.
    if len(set(s)) == 1:
        results.append("NO")
        continue

    # Convert to list for easier swapping.
    s_list = list(s)
    i = 0
    j = n - 1
    swapped = False

    # Two pointer approach: try to find a pair where s[i] != s[j].
    # For a non-palindrome, the first differing pair must have s[i] > s[j] (since s is not universal).
    # In that case a swap between s[i] and s[j] will fix the string.
    while i < j and k > 0:
        if s_list[i] == s_list[j]:
            i += 1
            j -= 1
            continue
        if s_list[i] > s_list[j]:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            k -= 1
            swapped = True
            break
        # If s_list[i] < s_list[j] then s would already be universal (by definition) so break.
        break

    new_s = "".join(s_list)
    # If the update fixed universality, we're done.
    if is_universal(new_s):
        results.append("YES")
    else:
        # If no swap was performed, then s is a palindrome.
        # For a non-constant palindrome a well-chosen swap always exists.
        # Here we assume that one swap can fix many palindromes.
        # In worst-case scenarios two swaps always suffice.
        if s == s[::-1]:
            # If you have at least one swap available (for a careful one–swap fix), then it is possible.
            results.append("YES" if k >= 1 else "NO")
        else:
            results.append("NO")

sys.stdout.write("\n".join(results))