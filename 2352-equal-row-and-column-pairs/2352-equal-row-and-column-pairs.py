class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowcounts =defaultdict(int)
        count =0
        
        for row in grid:
            rowcounts[tuple(row)]+=1
        for column in zip(*grid):
            count += rowcounts[column]
            
        return count
        