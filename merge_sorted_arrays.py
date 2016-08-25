class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # copy nums1 out of the way
        for idx in reversed(range(m)):
            nums1[idx + n] = nums1[idx]
        # merge
        idx1 = n
        idx2 = 0
        for idx in range(m + n):
            if idx1 < (m + n) and idx2 < n:
                if nums1[idx1] < nums2[idx2]:
                    nums1[idx] = nums1[idx1]
                    idx1 += 1
                else:
                    nums1[idx] = nums2[idx2]
                    idx2 += 1
            # could do this better by having a "fill in the rest of the array function
            elif idx2 < n:
                nums1[idx] = nums2[idx2]
                idx2 += 1

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

doer = Solution()
arr1 = [1,2,4,5,6,0]
arr2 = [3]
doer.merge(arr1,5,arr2,1)
print(arr1)