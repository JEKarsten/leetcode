class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mappings = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }
        
        length = len(digits)        
        result = []
        
        if length > 0:
            for a in mappings[digits[0]]:
                if length > 1:
                    for b in mappings[digits[1]]:
                        if length > 2:
                            for c in mappings[digits[2]]:
                                if length > 3:
                                    for d in mappings[digits[3]]:
                                        result.append(a+b+c+d)
                                else:
                                    result.append(a+b+c)
                        else:
                            result.append(a+b)
                else:
                    result.append(a)
        
        return result