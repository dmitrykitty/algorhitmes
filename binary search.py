def binary_search(lst, item):
   left = 0
   right = len(lst) - 1
   while left <= right:
       mid = (left + right) // 2
       guess = mid
       if guess == item:
           return guess
       elif guess > item:
           right = mid - 1
       else:
           left = mid + 1






lst = [a for a in range(100)]
print(binary_search(lst, 10)) #O(log2 od n)
#jezeli długosc np 100 --> (6.4556345)int + 1

def findInsertPosition(heights: List[int], new_height: int) -> int:
    left = 0;
    right = len(heights) - 1
    while left <= right:
        mid = (right + left) // 2
        if mid > 0 and heights[mid - 1] < new_height < heights[mid]:
            return mid
        elif new_height > heights[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left