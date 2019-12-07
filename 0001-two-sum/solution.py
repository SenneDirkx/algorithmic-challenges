class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        historicNums = {};
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in historicNums:
                return [historicNums[complement], i]
            historicNums[nums[i]] = i

# Runtime: 48 ms (faster than 93.52% of online Python3 submissions)
# Memory Usage: 13.9 MB (less than 66.05% of Python3 online submissions)