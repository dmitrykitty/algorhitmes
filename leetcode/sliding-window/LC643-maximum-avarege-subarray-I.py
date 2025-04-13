def findMaxAverage(nums, k):
    begin = 0
    window_state = 0
    result = float('-inf')

    for end in range(len(nums)):
        window_state += nums[end]
        if end - begin + 1 == k:
            # length of win
            result = max(result, window_state)
            window_state -= nums[begin]
            begin += 1

    return float(result) / k