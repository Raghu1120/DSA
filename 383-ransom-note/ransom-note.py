class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = defaultdict(int)
        for ch in magazine:
            freq[ch] += 1
        for c in ransomNote:
            if c not in freq:
                return False
            elif freq[c] == 1:
                del freq[c]
            else:
                freq[c] -= 1
        return True