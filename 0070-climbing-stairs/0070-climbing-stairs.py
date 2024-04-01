class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        dp=[1]*(n)
        dp[0]=1
        dp[1]=2
        for i in range(2,len(dp)):
            dp[i]=dp[i-2]+dp[i-1]
        return dp[-1]
        