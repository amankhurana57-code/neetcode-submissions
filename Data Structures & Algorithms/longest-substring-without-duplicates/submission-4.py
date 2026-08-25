class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 ## answer
        chr_set = set()
        l = 0 ###left most
        

        for r in range(len(s)): ###sliding window
            while s[r] in chr_set:
                chr_set.remove(s[l])
                l+=1
            chr_set.add(s[r])
            res = max(res,r-l+1)
        return res


                
           




        