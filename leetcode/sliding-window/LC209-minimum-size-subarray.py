def minSubArrayLen(self, target, nums):
    begin = 0
    result = float('inf')
    nums_sum = 0

    for end in range(len(nums)):
        nums_sum += nums[end]

        while nums_sum >= target:
            windows_size = end - begin + 1
            result = min(windows_size, result)
            nums_sum -= nums[begin]
            begin += 1

    if result == float('inf'):
        return 0
    return result