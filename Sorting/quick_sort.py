def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    if len(arr) == 2:
        return [arr[0], arr[1]] if arr[0] < arr[1] else [arr[1], arr[0]]

    pivot = arr[0]
    left, right = [], []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


assert (quick_sort([])) == []
assert (quick_sort([4, 51, 6, 1])) == [1, 4, 6, 51]
assert (quick_sort([4, 51, 6, 1, 60])) == [1, 4, 6, 51, 60]
assert (quick_sort([0, 0, 0])) == [0, 0, 0]
