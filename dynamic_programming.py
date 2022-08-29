############ Min Most Climbing Stairs ########
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:          
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
            print(cost[i])  
        return min(cost[-1],cost[-2])

 ###############################################
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2]) 
        return min(cost[0],cost[1])
########################################
########## Problem Number 70 ################
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.insert(i, dp[i - 1] + dp[i - 2])
            
        return dp[n] 
