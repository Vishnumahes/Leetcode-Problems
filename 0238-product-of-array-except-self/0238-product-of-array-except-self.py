class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Output=[1]*len(nums)
        pre=1
        for i in range (len(nums)):
            Output[i]=pre
            pre=pre*nums[i]
        suf =1
        for i in range (len(nums)-1,-1,-1):
            Output[i] =Output[i]*suf
            suf =suf*nums[i]
        return Output
            
        