# Question 23: Sort and then merge overlapping intervals.

def sort_and_merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]
merged_intervals = sort_and_merge_intervals(intervals)
print("Merged intervals:", merged_intervals)

intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
merged_intervals = sort_and_merge_intervals(intervals)
print("Merged intervals:", merged_intervals)