class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for count, val in enumerate(nums):
            if val in hashmap:
                 return True
            else :
                hashmap[val] =1
        return False





        