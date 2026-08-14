class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            dictTarget = target - nums[i]
            if dictTarget in map:
                return [map[dictTarget], i]
            map[nums[i]] = i
        

