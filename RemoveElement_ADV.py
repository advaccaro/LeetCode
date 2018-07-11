# LeetCode - 27. Remove Element
# Adam Vaccaro
# Accepted on June 30, 2018
# Runtime: 36ms
# Beat 100.00% of python3 submissions.

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return(len(nums))