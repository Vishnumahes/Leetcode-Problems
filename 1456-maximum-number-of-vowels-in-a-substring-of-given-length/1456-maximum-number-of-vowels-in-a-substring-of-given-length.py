class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel ={'a','e','i','o','u'}
        
        l,res,cnt = 0, 0 , 0
        
        for r in range(len(s)):
            if s[r] in vowel:
                cnt+=1
            if r-l+1 > k:
                if s[l] in vowel:
                    cnt -=1
                l+=1
            res = max(res, cnt)
        return res

    