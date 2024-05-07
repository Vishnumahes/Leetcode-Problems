class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF= 10 ** 20
        S1= INF
        S2= INF
        
        for x in nums:
            if x > S2:
                return True
            elif x > S1:
                S2=min(x,S2)
            S1=min(x,S1)
        return False
        