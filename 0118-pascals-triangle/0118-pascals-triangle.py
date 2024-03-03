class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result =[[1]]
        for i in range(numRows-1):
            temp =[0]+result[-1]+[0]
            temp_res=[]
            for i in range(len(temp)-1):
                temp_res.append(temp[i]+temp[i+1])
            result.append(temp_res)
        return result
                
            
        