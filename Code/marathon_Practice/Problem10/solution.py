class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev1 = nums[0]
        prev2 = max(nums[1],nums[0])
        res = 0
        for i in range(2, len(nums)):
            temp = prev2
            prev2 = max(prev2, prev1 + nums[i])
            prev1 = temp
        return prev2
            