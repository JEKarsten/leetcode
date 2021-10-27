class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return [""]
        result = []
        for c in xrange(n):
            for l in self.generateParenthesis(c):
                for r in self.generateParenthesis(n - 1 - c):
                    result.append('({}){}'.format(l, r))
        
        return result