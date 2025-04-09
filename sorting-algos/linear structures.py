# linked list
# każdy element ma adres na kolejny, nie są położone w nieprzerwanym ciągu pamięci, nie można wywoływac się przez index
# sequential access - one by one

# array - random access (by index)

#           arrays     lists
# reading    O(1)       O(n)
# insertion  O(n)       O(1)
# deletion   O(n)       O(1)

def selection_sort(lst):
    n = 0
    for i in range(len(lst) - 1):
        min_value_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_value_index] > lst[j]:
                min_value_index = j
            n += 1
        lst[i], lst[min_value_index] = lst[min_value_index], lst[i]
    print(n)
    return lst


def bubble_sort(lst):
    n = 0
    for i in range(len(lst) - 1):
        for j in range(0, len(lst) - 1 - i):
            n += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(n)
    return lst


def insertion_sort(lst):
    n = 0
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            n += 1
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    print(n)
    return lst


def insertion_sort2(lst):
    for i in range(1, len(lst)):
        j = i
        while lst[j - 1] > lst[j] and j > 0:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1

    return lst

def insertion_sort3(lst):
    for i in range(1, len(lst)):
        j = i
        while lst[j - 1] < lst[j] and j > 0:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst



lst1 = [34, 1, 23, 4, 56, 3, 78, 12]
lst2 = lst1[:]
lst3 = lst1[:]
lst4 = lst1[:]
lst5 = lst1[:]
print(selection_sort(lst1))
print(bubble_sort(lst2))
print(insertion_sort(lst3))
print(insertion_sort2(lst4))
print(insertion_sort3(lst3))
