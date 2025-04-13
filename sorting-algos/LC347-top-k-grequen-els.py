import heapq

def topKFrequent_0_to_100(nums, k: int):
    max_val = nums[0]
    for i in range(1, len(nums)):
        max_val = max(max_val, nums[i])

    a = [0] * (max_val + 1)

    for i in range(len(nums)):
        a[nums[i]] += 1

    c = [(-a[ind], ind) for ind in range(len(a))]
    heapq.heapify(c)

    res = [heapq.heappop(c)[1] for i in range(k)]
    return res



lst = [1,1,1,2,2,3]
print(topKFrequent_0_to_100(lst, 2))
