# Question 12: Sort an array of strings by their length.
def sort_strings_by_length(strings):
    length_map = {}

    for s in strings:
        length = len(s)
        if length not in length_map:
            length_map[length] = []
        length_map[length].append(s)
    sorted_lengths = sorted(length_map.keys())

    result = []
    for length in sorted_lengths:
        result.extend(length_map[length])

    return result

if __name__ == "__main__":
    strings = ["apple", "banana", "kiwi", "grape", "orange"]
    sorted_strings = sort_strings_by_length(strings)
    print("Sorted strings:", sorted_strings)