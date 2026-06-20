class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map_ = {}

        for idx, num in enumerate(nums):

            diff = target - num

            if diff in map_ and map_[diff] != idx:
                return [map_[diff], idx]

            map_[num] = idx

        return [-1,-1]
        