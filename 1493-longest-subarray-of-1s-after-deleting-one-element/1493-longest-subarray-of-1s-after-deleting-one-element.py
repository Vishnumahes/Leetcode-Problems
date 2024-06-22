class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,zero=0,1
        for r in range(len(nums)):
            if nums[r]==0:
                zero-=1
            if zero<0:
                zero+=nums[l]==0
                l+=1
        return r-l
                
        