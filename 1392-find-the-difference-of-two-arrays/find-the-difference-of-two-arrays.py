class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = []
        n1 = []
        n2 = []

        for n in nums1:
            if n not in nums2 and n not in n1:
                n1.append(n)
            else:
                pass
            
        for n in nums2:
            if n not in nums1 and n not in n2:
                n2.append(n)
            else:
                pass
        answer.append(n1)
        answer.append(n2)
        return answer