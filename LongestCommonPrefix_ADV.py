# LeetCode - 14. Longest Common Prefix
# Adam Vaccaro
# Accepted on July 10, 2018
# Runtime: 40ms
# Beat 90.87% of python3 submissions.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0:
            return(prefix)
        min_len = min([len(string) for string in strs])
        for j in range(min_len):
            current_letters = [string[j] for string in strs]
            if all(letter == current_letters[0] for letter in current_letters):
                prefix += str(current_letters[0])
            else:
                return(prefix)
        return(prefix)
            
        