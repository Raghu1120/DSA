class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for num in range(n-1,-1,-1):
            if digits[num] < 9:
                digits[num] +=1
                return digits
            digits[num] = 0
        return [1] + digits