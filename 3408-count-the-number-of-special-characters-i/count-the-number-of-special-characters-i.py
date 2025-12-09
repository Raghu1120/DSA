class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        for i,ch in enumerate(word):
            if ch not in lower and ch.islower():
                lower[ch] = i
            elif ch.isupper() and ch not in upper:
                upper[ch] = i
        count = 0

        for c in range(26):
            low = chr(ord('a')+c)
            up = chr(ord('A')+c)

            if low in lower and up in upper :
                count += 1
        return count

        