class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max = 0
        for candy in candies:
            if candy>=max:
                max=candy
        o = []
        isValid = True
        for c in candies:
            if c+extraCandies >= max:
                o.append(isValid)
            else:
                o.append(not isValid)
        return o
                