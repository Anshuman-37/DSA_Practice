# Question 18: Find the k closest points to the origin using a max-heap.
import heapq


def k_closest_points_to_origin(points, k):
    max_heap = []

    for point in points:
        x, y = point
        dist_sq = x ** 2 + y ** 2

        if len(max_heap) < k:
            heapq.heappush(max_heap, (-dist_sq, point))
        else:
            if -dist_sq > max_heap[0][0]:
                heapq.heapreplace(max_heap, (-dist_sq, point))

    closest_points = [point for _, point in max_heap]
    return closest_points


points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
closest = k_closest_points_to_origin(points, k)
print(f"The {k} closest points are: {closest}")
