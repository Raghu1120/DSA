class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for val in nums:
            if val in hashmap:
                return True
            hashmap[val] = True

        return False


        