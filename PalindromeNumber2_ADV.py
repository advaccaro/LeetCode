# LeetCode - 9. Palindrome Number (without conversion to string)
# Adam Vaccaro
# Accepted on July 10, 2018
# Runtime: 300ms
# Beat 64.90% of python3 submissions.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return(False)
        num = x
        nums = []
        while num > 0:
            nums.append(num % 10)
            num = int(num / 10)
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == nums[j]:
                i+=1
                j-=1
                continue
            return False
        return True