class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        ans = [] 
        
        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if not ans or ans[-1][1] < start:
                ans.append([start, end])  
            else:
                ans[-1][1] = max(ans[-1][1], end)
        
        return ans
        