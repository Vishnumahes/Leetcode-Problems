class Solution:
    def jump(self, nums: List[int]) -> int:
        l=0
        r=0
        res=0
        while r <len(nums)-1:
            m=0
            for i in range(l,r+1):
                if nums[i]+i>m:
                    m=i+nums[i]
            l=r+1
            r=m
            res+=+1
        return res
                
        