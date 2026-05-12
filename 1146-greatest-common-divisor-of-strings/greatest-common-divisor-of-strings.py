import math
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)
        
        def divides(length):
            if len1 % length != 0 or len2 % length != 0:
                return False
            f1 = len1 // length 
            f2 = len2 // length
            return str1[:length] * f1 == str1 and str1[:length] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if divides(l):
                return str1[:l]
        
        return ""
        
        