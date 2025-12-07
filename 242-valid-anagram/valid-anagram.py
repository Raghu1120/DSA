class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False
        for num in s:
            freq[num] = freq.get(num,0)+1
        for num in t:
            freq[num] = freq.get(num,0)-1
            
        for char,count in freq.items():
            if count != 0:
                return False
        return True