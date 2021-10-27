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
        
        if length == 4:
            for a in mappings[digits[0]]:
                for b in mappings[digits[1]]:
                    for c in mappings[digits[2]]:
                        for d in mappings[digits[3]]:
                            result.append(a+b+c+d)
            return result
        elif length == 3:
            for a in mappings[digits[0]]:
                for b in mappings[digits[1]]:
                    for c in mappings[digits[2]]:
                        result.append(a+b+c)
            return result
        elif length == 2:
            for a in mappings[digits[0]]:
                for b in mappings[digits[1]]:
                    result.append(a+b)
            return result
        elif length == 1:
            for a in mappings[digits[0]]:
                result.append(a)
            return result
        
        return result
        