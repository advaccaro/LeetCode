# LeetCode - 20. Valid Parentheses
# Adam Vaccaro
# Accepted on July 10, 2018
# Runtime: 36ms
# Beat 99.99% of python3 submissions.

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 == 1:
            return(False)
        
        back_dict = {}
        back_dict[")"] = "("
        back_dict["]"] = "["
        back_dict["}"] = "{"

        openers = ["(", "[", "{"]
        closers = [")", "]", "}"]
        check_str = ""
        j = 0
        while j < n:
            c = s[j]
            if j == 0:
                if c in closers: return(False)
                check_str += c
                j += 1
                
            elif j == n-1:
                if c in openers: 
                    return(False)
                elif back_dict[c] != check_str[-1]: 
                    return(False)
                check_str += c
                j += 1
            else:
                if c in openers:
                    check_str += c
                if c in closers:
                    if back_dict[c] != check_str[-1]:
                        return(False)
                    elif back_dict[c] == check_str[-1]:
                        check_str = check_str[:-1]
                j += 1
        return(True)
