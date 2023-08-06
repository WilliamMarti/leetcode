class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 1
        for num1 in range(0, len(nums)):
            for num2 in range(i, len(nums)):
                if nums[num1] + nums[num2] == target:
                    return [num1, num2]
            i += 1