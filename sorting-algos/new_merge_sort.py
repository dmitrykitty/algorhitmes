def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)
    return arr


def merge(arr, l, mid, r):
    left = arr[l: mid + 1]
    right = arr[mid + 1: r + 1]

    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [2, 5, 12, 4, -3, 1, 6, 45]


print(merge_sort(arr, 0, len(arr) - 1))