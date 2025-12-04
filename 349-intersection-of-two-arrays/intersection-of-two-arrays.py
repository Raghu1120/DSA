class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        resarr = []
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    resarr.append(nums1[i])
        return list(set(resarr))

        

        