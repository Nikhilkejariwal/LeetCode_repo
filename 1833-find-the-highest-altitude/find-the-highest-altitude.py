class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = [0]
        s=0
        for g in gain:
            s += g
            alt.append(s)
        max = 0
        o = 0
        for a in alt:
            if a>o:
                o=a
        return o