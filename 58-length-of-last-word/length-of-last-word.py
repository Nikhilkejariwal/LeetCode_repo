class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(" ")
        f = []
        for n in s:
            if n == '':
                pass
            else:
                f.append(n)
        l = f[len(f)-1]
        return (len(l))

        