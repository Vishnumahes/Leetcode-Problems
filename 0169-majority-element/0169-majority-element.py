class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                element = num
            count += 1 if num == element else -1
        
        # Verifying the majority element
        count = 0
        for num in nums:
            if num == element:
                count += 1
        
        if count > len(nums) // 2:
            return element
                
                
        