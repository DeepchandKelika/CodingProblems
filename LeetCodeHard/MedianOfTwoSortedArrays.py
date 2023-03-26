#https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#Leetcode difficulty level: Hard

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        l = len(nums3)
        if l%2 == 1:
            median = nums3[(len(nums3)-1)//2]
        else:
            median =( nums3[l//2]+nums3[l//2 - 1]) / 2
        return median
