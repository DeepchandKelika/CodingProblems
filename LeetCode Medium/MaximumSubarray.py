#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        l = len(nums)
        current = nums[0]
        for i in range(1,l):
            current = max(nums[i],current + nums[i])
            maxx = max(current, maxx)
        return maxx
