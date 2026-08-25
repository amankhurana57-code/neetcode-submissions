class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letterdict =  {} ##char:count
        for s in s1:
            if s in letterdict:
                letterdict[s] +=1
            else:
                letterdict[s] = 1
        letterdict = sorted(letterdict.items())


        
        for itr1 in range(len(s2)):
            currentdict = {}
            subset = s2[itr1:itr1+len(s1)]
            for itr2 in subset:
                if itr2 in currentdict:
                    currentdict[itr2]+=1
                else:
                    currentdict[itr2] = 1
            currentdict = sorted(currentdict.items())

            if currentdict == letterdict:
                return True
        return False
            
    



        
        