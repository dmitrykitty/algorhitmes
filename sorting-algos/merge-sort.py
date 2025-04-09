def merge_sort(arr):
    if len(arr) > 1:
        left = arr[: len(arr) // 2]
        right = arr[len(arr) // 2 :]

        #recursive
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

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


def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right) #zwraca index pivot poin
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)

def partition(arr, left, right):
     i = left
     j = right - 1
     piv = arr[right]

     while i < j:
        while i < right and arr[i] < piv:
            i += 1
        while j > left and arr[j] >= piv:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
     if arr[i] > piv:
         arr[i], arr[right] = arr[right],  arr[i]

     return i


ar_test = [2, 1, 2, 7, 5, 8, 3, 1, 5, 6, 9]
ar_test2 = ar_test[:]

quick_sort(ar_test2, 0, len(ar_test2))
print(ar_test2 )

merge_sort(ar_test)
print(ar_test)