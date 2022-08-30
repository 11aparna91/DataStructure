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
############### Space Complexity=O(m*n) #############
##############  Problem Number 62 ###################
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1,m):   ## consider reverse matrix
            for j in range(1,n):
                dp[i][j]= dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
