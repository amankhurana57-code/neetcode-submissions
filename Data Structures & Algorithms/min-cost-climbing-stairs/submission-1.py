class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        final = [0] * n
        final[n-1] = cost[n-1]
        final[n-2] = cost[n-2]

        for i in range(n-3,-1,-1):
            final[i] = min((cost[i] + final[i+1]), (cost[i] + final[i+2]))

        return min(final[0],final[1])


        