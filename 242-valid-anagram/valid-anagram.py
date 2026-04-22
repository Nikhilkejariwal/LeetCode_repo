class Solution(object):
    def isAnagram(self, first, second):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = []
        s2 = []
        if len(first) != len(second):
            return False
        for f in first:
            s1.append(f)
        for s in second:
            s2.append(s)
        for i in range(len(s2)):
            if s2[i] not in s1:
                return False
            if s2[i] in s1:
                s1.remove(s2[i])
        return True
               

        

        