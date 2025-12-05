class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            square = num * num
            res.append(square)
        res.sort()
        return res

        