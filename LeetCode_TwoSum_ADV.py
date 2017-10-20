# LeetCode - Two Sum
# https://leetcode.com/problems/two-sum/description/
# Adam Vaccaro

class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
		You may assume that each input would have exactly one solution, and you may not use the same element twice.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for num in nums:
        	num_ind = nums.index(num)
        	reduced_nums_inds = list(set([i for i in range(len(nums))]) - set([num_ind]))
        	for ind in reduced_nums_inds:
        		if nums[num_ind] + nums[ind] == target:
        			return([num_ind, ind])
        		
        print('No solution found.')


if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	target = 9
	answer = Solution.twoSum(Solution,nums,target)
	print(answer)
 	

