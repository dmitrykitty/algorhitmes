def countingSort(array, k):
    n = len(array)
    c = [0] * k
    output = [0] * n
    for i in range(n):
        c[array[i]] = c[array[i]] + 1

    for i in range(1, k):
        c[i] = c[i] + c[i - 1]

    for i in range(n - 1, -1, -1):
        output[c[array[i]] - 1] = array[i]
        c[array[i]] = c[array[i]]  - 1
    return output

arr1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
new_ar1 = countingSort(arr1, 7)
print(new_ar1)

def countingSort2(array, k):
    n = len(array)
    c = [0] * k
    c1, c2, c3 = 0, 0, 0
    output = [0] * n
    for i in range(n):
        c1 += 1
        c[array[i]] = c[array[i]] + 1

    for i in range(1, k):
        c2 += 1
        c[i] = c[i] + c[i - 1]

    for i in range(n):
        c3 += 1
        output[c[array[i]] - 1] = array[i]
        c[array[i]] = c[array[i]]  - 1

    print(c1, c2, c3)
    return output

arr2 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
new_ar2 = countingSort2(arr2, 7)
print(new_ar2)