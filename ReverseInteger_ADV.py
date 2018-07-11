# LeetCode - 7. Reverse Integer
# Adam Vaccaro
# Accepted on July 10, 2018
# Runtime: 56ms
# Beat 98.48% of python3 submissions.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        if x_str[0] == "-":
            x_str_clip = x_str[1:]
            x_str_clip_rev = x_str_clip[::-1]
            x_rev = int("-" + x_str_clip_rev)
        else:
            x_rev = int(x_str[::-1])
        if abs(x_rev) > 2**31 :
            return(0)
        else:
            return(x_rev)

