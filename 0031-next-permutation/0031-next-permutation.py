class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
    # If such an element is found, find the smallest element from the right that is greater than it
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
        # Swap the two elements
            nums[i], nums[j] = nums[j], nums[i]
    # Reverse the elements from i+1 to the end to get the next permutation
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        