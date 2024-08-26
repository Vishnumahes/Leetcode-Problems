class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                k = j + 1
                l = n - 1

                while k < l:
                    csum = nums[i] + nums[j] + nums[k] + nums[l]
                    if csum == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        
                        # Skip duplicates for the third element
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        # Skip duplicates for the fourth element
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        
                        # Move pointers to the next unique elements
                        k += 1
                        l -= 1
                    elif csum < target:
                        k += 1
                    else:
                        l -= 1
                        
        return result
