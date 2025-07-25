class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest =0
        numSet = set(nums)
        for n in numSet:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length +=1
                longest = max(length, longest)
        return longest
        