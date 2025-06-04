class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = 0
        maximum = nums[0]
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > maximum:
                maximum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return maximum
