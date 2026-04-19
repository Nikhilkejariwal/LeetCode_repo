class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        left = 0
        right = len(s) - 1

        while left<right:
            if s[left] != s[right]:
                return False
            left = left+1   # How does left move?
            right = right-1  # How does right move?

        return True  # When do you know it's a palindrome?

        




        