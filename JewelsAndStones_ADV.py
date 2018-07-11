# LeetCode - 771. Jewels And Stones
# Adam Vaccaro
# Accepted on July 10, 2018
# Runtime: 40ms
# Beat 99.94% of python3 submissions.

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for c in S:
            if c in J: count += 1
        return(count)