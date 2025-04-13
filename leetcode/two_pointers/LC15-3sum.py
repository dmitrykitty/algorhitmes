def threeSum(nums):
    nums = sorted(nums)
    lst = []
    for i in range(len(nums) - 1):
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                lst.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    return lst


num = [-1,0,1,2,-1,-4]
print(threeSum(num))