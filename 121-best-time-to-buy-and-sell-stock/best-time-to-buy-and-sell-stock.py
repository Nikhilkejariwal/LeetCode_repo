class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minVal = prices[0]
        maxVal = 0
        for p in prices:
            if p<minVal:
                minVal = p
            current = p - minVal
            if current>maxVal:
                maxVal = current
        return maxVal