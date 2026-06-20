class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}

        for i in range(len(nums)):
            look = target - nums[i]

            if look in map_ and map_[look] != i:
                return [map_[look],i]

            map_[nums[i]] = i

        return [-1,-1]
            