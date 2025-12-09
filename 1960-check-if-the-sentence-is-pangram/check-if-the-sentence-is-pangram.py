class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        count = 0
        hashmap = {}
        for i, ch in enumerate(sentence):
            hashmap[ch] = i
        
        for c in range(26):
            alphabet = chr(ord('a')+c)

            if alphabet in hashmap:
                count+=1

        if count < 26:
            return False
        return True
        
