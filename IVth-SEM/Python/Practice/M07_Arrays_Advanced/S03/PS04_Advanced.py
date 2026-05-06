from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s1 = nums[0]
        s2 = nums[0]
        for i in range(1, len(nums)):
            s1 = max(nums[i], s1 + nums[i])
            s2 = max(s1, s2)
        return s2