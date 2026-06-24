class Solution(object):
    def mergeAlternately(self, word1, word2):
        """

        :type word1: str
        :type word2: str
        :rtype: str
        """
        word = []
        minLen = min(len(word1),len(word2))
        for i in range(minLen):
            word.append(word1[i])
            word.append(word2[i])
            
        return ("".join(word) + word1[minLen:] + word2[minLen:])
        