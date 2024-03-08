class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range (len(nums)):
            if nums[i]==target:
                return i
            else:
                if nums[i]!=target:
                    x=target
                    nums.append(x)
                    nums.sort()
                    return nums.index(x)
            
                    
        