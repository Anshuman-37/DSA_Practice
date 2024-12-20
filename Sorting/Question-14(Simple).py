# Question 4: Sort elements by their frequency.
from collections import Counter


def sort_by_frequency(arr):
    count = Counter(arr)

    # (frequency, element) pairs (Use -ve freq to get descending order)
    freq_list = [(freq, num) for num, freq in count.items()]

    # Sort by frequency (descending) and then by element (ascending)
    freq_list.sort()

    result = []
    for freq, num in freq_list:
        result.extend([num] * freq)

    return result

arr = [2, 5, 2, 8, 5, 6, 8, 8,1]
print(sort_by_frequency(arr))