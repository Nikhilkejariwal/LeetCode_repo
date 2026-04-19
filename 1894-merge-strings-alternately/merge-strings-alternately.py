class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                m+=word1[i]+word2[i]
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                m+=word1[i]+word2[i]
            m+=word1[i+1:]
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                m+=word1[i]+word2[i]
            m+=word2[i+1:]
            
        return m
                