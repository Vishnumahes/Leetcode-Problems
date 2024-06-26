class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)
        v1,v2 = sorted(cnt1.values()),sorted(cnt2.values())
        
        
        return set(word1)== set(word2) and v1==v2
        