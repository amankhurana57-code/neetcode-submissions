class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ### only add open parenthsis open openN < openN
        ## only add closed parenthis when closedN < openN
        ##valid of openN == closedN
        res = []
        stack = []
        def dfs(openN, closedN):

            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                dfs(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN+1)
                stack.pop()
            
        dfs(0,0)

        return res


        