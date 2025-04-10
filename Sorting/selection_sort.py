def get_smallest_index(arr: list) -> int:
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    sorted_array = []
    for _ in range(len(arr)):
        smallest_index = get_smallest_index(arr)
        sorted_array.append(arr.pop(smallest_index))
    return sorted_array


assert (selection_sort([])) == []
assert (selection_sort([4, 51, 6, 1])) == [1, 4, 6, 51]
assert (selection_sort([0, 0, 0])) == [0, 0, 0]
