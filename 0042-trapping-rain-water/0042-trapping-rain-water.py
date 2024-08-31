class Solution:
    def trap(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        maxleft=maxright=0
        res=0
        
        while(left<=right):
            if(arr[left]<=arr[right]):
                if(arr[left]>=maxleft):
                    maxleft=arr[left]
                else:
                    res+=maxleft-arr[left]
                left+=1
            else:
                if(arr[right]>=maxright):
                    maxright=arr[right]
                else:
                    res+=maxright-arr[right]
                right-=1
        return res
        
        