class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            m , n = n, m
            nums1, nums2 = nums2, nums1

        left, right = 0, m

        while left <= right:
            pA = (left + right) // 2
            pB = (m + n + 1) // 2 - pA

            maxleftA = nums1[pA - 1] if pA - 1 >= 0 else float('-inf')
            minrightA = nums1[pA] if pA < m else float('inf')
            maxleftB = nums2[pB - 1] if pB - 1 >= 0 else float('-inf')
            minrightB = nums2[pB] if pB < n else float('inf')

            if maxleftA > minrightB:
                right = pA - 1
            if maxleftB > minrightA:
                left = pA + 1
            if maxleftA <= minrightB and maxleftB <= minrightA:
                if (m+n) % 2==0:
                    return (max(maxleftA, maxleftB) + min(minrightA, minrightB))/2
                else:
                    return max(maxleftA, maxleftB)

        
        