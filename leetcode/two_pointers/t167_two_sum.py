class Solution(object):
    def twoSum(self, numbers, target):
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] not in dic:
                dic[target - numbers[i]] = i
            else:
                return [dic[numbers[i]] + 1, i + 1]


S = Solution()
print(S.twoSum([2,7,11,15], 9))


def twoSum2(nums, target):
    d = {}
    for i in range(len(nums)):
        second = target - nums[i]
        if nums[i] in d:
            return [d[nums[i]], i]
        else:
            d[second] = i

print(twoSum2([2,7,11,15], 9))
