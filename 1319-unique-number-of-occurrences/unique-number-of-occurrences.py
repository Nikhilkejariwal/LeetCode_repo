class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = []
        for a in arr:
            if a not in n:
                n.append(a)
        print(n)
        occ = []
        for i in range(len(n)):
            count = 0
            for j in range(len(arr)):
                if n[i] == arr[j]:
                    count = count + 1
            occ.append(count)
        print(occ)
        isValid = True
        c = 0
        for o in occ:
            if o not in occ:
                pass
            else:
                c = c+1
        if c == len(set(occ)):
            isValid = True
        else:
            isValid = False
        return isValid