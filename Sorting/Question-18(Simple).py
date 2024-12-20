# Question 18: Implement Bucket Sort for floating-point numbers in [0,1].

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for x in arr:
        index = int(n * x)
        buckets[index].append(x)

    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)