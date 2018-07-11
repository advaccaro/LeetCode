# LeetCode - 28. Implement strStr()
# Adam Vaccaro
# Accepted on June 30, 2018
# Runtime: 40ms
# Beat 63.74% of python3 submissions.

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":  return(0)
        elif needle not in haystack: return(-1)
        else: return(haystack.index(needle))