# LeetCode - 9. Palindrome Number (with conversion to string)
# Adam Vaccaro
# Accepted on July 10, 2018
# Runtime: 268ms
# Beat 99.17% of python3 submissions.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return(str(x) == str(x)[::-1])