def insertion_sort(data: list):
    for i in range(1, len(data)):
        j = i - 1
        key = data[i]

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


def merge(left: list, right: list):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort(data: list):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)


def max_heapify(data: list, size: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if (left < size) and (data[left] > data[largest]):
        largest = left

    if (right < size) and (data[right] > data[largest]):
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        max_heapify(data, size, largest)


def heap_sort(data: list):
    size = len(data)
    for i in range(size // 2, -1, -1):
        max_heapify(data, size, i)

    for i in range(size - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        max_heapify(data, i, 0)

    return data


def partition(data: list, left: int, right: int):
    pivot = data[right]
    i = left - 1

    for j in range(left, right):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[right] = data[right], data[i + 1]

    return i + 1


def quick_sort(data: list, left: int, right: int):
    """
    Start with (data, 0, len(data)-1)
    """
    if left < right:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot - 1)
        quick_sort(data, pivot + 1, right)

    return data
