class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution = []
        count = 0
        reached = True
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    solution.append(i)
                    solution.append(j)     
        return solution


