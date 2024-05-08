class Solution:
    def compress(self, chars: List[str]) -> int:
        i,r=0,0
        
        
        while i<len(chars):
            currChar =chars[i]
            curroc=0
            while((i<len(chars)) and (chars[i]==currChar)):
                i+=1
                curroc+=1
                
            chars[r]= currChar
            r+=1
            if(curroc>1):
                currocStr=str(curroc)
                for j in range(len(currocStr)):
                    chars[r]=currocStr[j]
                    r+=1
        return r
            
                
        