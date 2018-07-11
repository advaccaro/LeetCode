# LeetCode - 35. Search Insert Position
# Adam Vaccaro
# Accepted on June 30, 2018
# Runtime: 36ms
# Beat 99.96% of python3 submissions.

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return(nums.index(target))
        else:
            nums.append(target)
            nums = sorted(nums)
            return(nums.index(target))