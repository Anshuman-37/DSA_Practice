import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # Handle edge case of n=0 if necessary, though constraints say n >= 1
    if n == 0:
        print(0)
        return

    initial_max = 0
    total_sum = 0
    count_odd = 0

    # Single pass to get sum, initial max, and odd count
    for x in a:
        total_sum += x
        if x > initial_max:
            initial_max = x
        if x % 2 != 0:
            count_odd += 1

    # Case 1: No operations possible (all elements have the same parity)
    if count_odd == 0 or count_odd == n:
        print(initial_max)
    else:
        # Case 2: Operations are possible (mix of parities)
        # Calculate the potential maximum if we reach the state where
        # all non-zeros are odd and occupy the initial 'odd' slots.
        max_final_odd = 0
        # This state is only possible if the total sum S has the same
        # parity as the number of odd elements count_odd.
        if total_sum % 2 == count_odd % 2:
            # If possible, the max value is S - (count_odd - 1)
            # S >= count_odd is implicitly true here because a_i >= 1
            # and count_odd > 0.
            max_final_odd = total_sum - count_odd + 1

        print(max(initial_max, max_final_odd))


t = int(sys.stdin.readline())
for _ in range(t):
    solve()