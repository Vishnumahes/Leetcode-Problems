class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        ctow={}
        wtoc={}
        for i in range(0,len(words)):
            if pattern[i] not in ctow:
                ctow[pattern[i]]=words[i]
            elif pattern[i] in ctow:
                value=ctow[pattern[i]]
                if value==words[i]:
                    continue
                else:
                    return False
            if words[i] not in wtoc:
                wtoc[words[i]]=pattern[i]
            elif words[i] in wtoc:
                value = wtoc[words[i]]
                if value ==pattern[i]:
                    continue
                else:
                    return False
        return True
                
        