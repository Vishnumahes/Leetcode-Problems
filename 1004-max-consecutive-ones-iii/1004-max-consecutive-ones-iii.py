class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, max_w ,non_zeros, l =0,0,0,0
        
        for r in range (len(nums)):
            if nums[r] == 0:
                non_zeros +=1
            while non_zeros > k:
                if nums[l]==0:
                    non_zeros -=1
                l+=1
            w= r-l+1
            max_w = max(max_w,w)
        return max_w
            
                
                
                
        
                
                
        