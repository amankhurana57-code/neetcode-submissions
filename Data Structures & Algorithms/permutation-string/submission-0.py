from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letterdict = Counter(s1)
        n = len(s1)
        
        for i in range(len(s2) - n + 1):
            currentdict = Counter(s2[i:i+n])
            if currentdict == letterdict:
                return True
            
        return False