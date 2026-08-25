class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans =[]
        n = len(nums)
        sol = []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans
        