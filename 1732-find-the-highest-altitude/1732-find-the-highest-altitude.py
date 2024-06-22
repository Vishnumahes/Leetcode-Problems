class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        great=0
        high=0
        
        for i in gain:
            great+=i
            high=max(great,high)
        return high
        