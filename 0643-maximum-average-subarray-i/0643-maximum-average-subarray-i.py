class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        currsum = 0
        
        for i in range(k):
            currsum += nums[i]
        maximumavg = currsum/k
        
        
        for i in range(k,n):
            currsum +=nums[i]
            currsum-=nums[i-k]
            
            avg =currsum /k
            maximumavg =max(avg,maximumavg)
            
        return maximumavg
        
    
        
        
        