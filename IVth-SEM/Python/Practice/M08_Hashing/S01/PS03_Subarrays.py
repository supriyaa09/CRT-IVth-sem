#Leetcode => 560
'''class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        result = 0
        c = {0: 1}
        for ele in nums:
            prefix_sum += ele
            if (prefix_sum - k) in c:
                result += c[prefix_sum - k]
            if prefix_sum in c:
                c[prefix_sum] += 1
            else:
                c[prefix_sum] = 1

        return result'''
