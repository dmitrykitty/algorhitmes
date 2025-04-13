def sortedSquares( nums):
    result = [0] * len(nums)
    left = 0
    nwptr = right = len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[nwptr] = nums[left] ** 2
            left += 1
        else:
            result[nwptr] = nums[right] ** 2
            right -= 1

        nwptr -= 1

    return result

lst = [-7,-3,2,3,11]
print(sortedSquares(lst))