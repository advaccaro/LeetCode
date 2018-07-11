# LeetCode - 26. Remove Duplicates from Sorted Array
# Adam Vaccaro
# Accepted on June 30, 2018
# Runtime: 700ms
# Beat 8.26% of mysql submissions.

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        j = 0
        while j < n:
            if nums[j] == nums[j+1]:
                nums.remove(nums[j])
                n -= 1
                continue
            else:
                j += 1
        return(len(nums))