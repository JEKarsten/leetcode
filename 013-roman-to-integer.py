class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s_list = []
        for d in s:
            s_list += [values[d]]
        for i in range(len(s_list) - 1):
            if s_list[i] < s_list[i + 1]:
                s_list[i] *= -1
        return sum(s_list)