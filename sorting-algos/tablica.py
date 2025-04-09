lst = [1, 2 ,3 ,4]
print(lst)
print(f"[{' '.join(map(str, lst))}]")


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    left = q - p + 1
    right = r - q
    L = arr[p:q + 1]
    R = arr[q + 1:r + 1]  # +1 dla wartownika

    print(f"([{' '.join(map(str, L))}] [{' '.join(map(str, R))}])")  # tu dlatego żeby wypisywało KAŻDY krok.

    L.append(float('inf'))
    R.append(float('inf'))  # wartownik infinity

    i = 0
    j = 0

    # for i in range (len(left)):
    #     L[i] = arr[p+i-1]
    # for j in range(len(right)):
    #     R[j] = arr[q+j]   #CORMEN

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

arr = [156, 271, 206, 84]
merge_sort(arr, 0, len(arr) - 1)