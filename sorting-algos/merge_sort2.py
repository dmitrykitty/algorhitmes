def print_ars(l_ar, r_ar):
    s1 = ' '.join(map(str, l_ar))
    s2 = ' '.join(map(str, r_ar))
    print(f"([{s1}] [{s2}])")

def merge_sort(arr, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(arr, p, q)
    merge_sort(arr, q + 1, r)
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    left = arr[p:q + 1]
    right = arr[q + 1:r + 1]
    print_ars(left, right)
    i = j = 0
    k = p
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
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


arr = [234, 141]
merge_sort(arr, 0, len(arr) - 1)

arr = [101, 6, 28]
merge_sort(arr, 0, len(arr) - 1)

arr = [156, 271, 206, 84]
merge_sort(arr, 0, len(arr) - 1)