# LeetCode - 1. Two Sum
# Adam Vaccaro
# Accepted on July 10, 2018
# Runtime: 6176ms
# Beat 8.022% of python3 submissions.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for num in nums:
            num_ind = nums.index(num)
            reduced_nums_inds = list(range(num_ind+1, n))
            for ind in reduced_nums_inds:
                if nums[num_ind] + nums[ind] == target:
                    return([num_ind, ind])