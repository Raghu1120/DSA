class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        mapST, mapTS = {}, {}
        
        for c1, c2 in zip(s, t):
            # check if mapping exists but inconsistent
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            
            # assign mapping
            mapST[c1] = c2
            mapTS[c2] = c1
        
        return True
