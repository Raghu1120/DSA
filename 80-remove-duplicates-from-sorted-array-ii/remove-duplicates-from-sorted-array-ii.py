class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 2
        for r in range(2, len(nums)):
            nums[l] = nums[r]

            if nums[l] != nums[l - 2]:
                l += 1

        return l

        
        