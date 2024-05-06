class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels ="aeiouAEIOU"
        
        li=list(s)
        
        i=0
        j=len(s)-1
        while (i<j):
            if li[i] not in vowels:
                i+=1
                continue
            if li[j] not in vowels:
                j-=1
                continue
            li[i],li[j]=li[j],li[i]
            i+=1
            j-=1
        return"".join(li)
        