class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(words) != len(pattern):
            return False
        hashp,hashs = {} , {}
        for c1,c2 in zip(pattern,words):
            if ((c1 in hashp and hashp[c1] != c2) or (c2 in hashs and hashs[c2] != c1)):
                return False
            hashp[c1] = c2
            hashs[c2] = c1
        return True
