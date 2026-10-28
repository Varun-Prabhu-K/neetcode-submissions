class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1, -1, -1):
            a = target - nums[i]
            if a in nums:
                return [nums.index(a), i]