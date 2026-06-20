class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_ = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in set_:
                length = 1
                while num + length in set_:
                    length += 1

                longest = max(length, longest)

        return longest

        