def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Sort and merge two halves
    return merge(left, right)


def merge(left: list, right: list) -> list:
    merged_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    return merged_array


assert (merge_sort([])) == []
assert (merge_sort([4, 51, 6, 1])) == [1, 4, 6, 51]
assert (merge_sort([0, 0, 0])) == [0, 0, 0]
