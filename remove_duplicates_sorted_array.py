# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        prev = None
        curr_idx = 0
        for num in nums:
            if num != prev:
                nums[curr_idx] = num
                curr_idx += 1
                prev = num
        return curr_idx


doer = Solution()
nums = [1]
print(doer.removeDuplicates(nums))
print(nums)