# LeetCode - 13. Roman to Integer
# Adam Vaccaro
# Accepted on July 10, 2018
# Runtime: 132ms
# Beat 99.14% of python3 submissions.

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {}
        roman_dict['I'] = 1
        roman_dict['V'] = 5
        roman_dict['X'] = 10
        roman_dict['L'] = 50
        roman_dict['C'] = 100
        roman_dict['D'] = 500
        roman_dict['M'] = 1000

        j = 0
        n = len(s) - 1
        int_sum = 0
        while j <= n:
            current_val = roman_dict[s[j]]
            if j != n:
                next_val = roman_dict[s[j + 1]]
                if current_val < next_val:
                    int_sum += next_val - current_val
                    j += 1
                else:
                    int_sum += current_val
            else:
                int_sum += current_val
            j += 1
        return(int_sum)
                
        