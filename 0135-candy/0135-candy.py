class Solution:
    def candy(self, ratings: List[int]) -> int:
        l=[1]*len(ratings)
        for i in range (1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                l[i]=l[i-1]+1
        for i in range (len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                m=max(l[i+1]+1,l[i])
                l[i]=m
        return sum(l)
            
                
        