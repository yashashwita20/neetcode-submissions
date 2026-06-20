class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums.sort()

        for i, num in enumerate(nums):

            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:

                sum_ = num + nums[left] + nums[right]

                if sum_ > 0:
                    right -= 1
                if sum_ < 0:
                    left += 1
                if sum_ == 0:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
        